#!/usr/bin/env python3
"""
GSIMA — Grantham–SWING IBAM–MyhT Analysis (n26, 60/90 dual-gate)
============================================================
Reconstructed from SWING_Validation_Methods_Results.md
Updated for corrected n26 cassette (Magallana C-term truncation fixed).

Core approach: We do NOT use SWING's full ML pipeline (Doc2Vec, XGBoost).
We extract only SWING's biochemical encoding principle:
    diff = round(abs(polarity_score(IBAM_aa) - polarity_score(MyhT_aa)))

For each cassette position and each taxon, we compute the mean polarity
difference of the IBAM residue against all positions of the MyhT sequence.
Cross-taxon standard deviation of these means is the conservation metric.
Low SD = the position has a biochemically consistent profile across all taxa.

This is orthogonal to the MD/IGE/PRCO-decode pipeline:
  - No structural data used
  - No AF3 predictions used
  - No MD trajectories used
  - Only raw sequences + Grantham polarity scores

Usage:
    python3 scripts/gsima_analysis.py \
        --cassette MG_projected_trimmed_n26_core60_chem90.fa \
        --myht_dir /path/to/myht_fastas/

MyhT FASTA files should be named: <Taxon_name>_MyhT.fa
(matching the taxon names in the cassette FASTA headers)

Siwek et al. Nature Methods 2025: https://doi.org/10.1038/s41592-025-02723-1
"""

import sys
import os
import argparse
import numpy as np
from collections import defaultdict
from datetime import datetime

# ─────────────────────────────────────────────
# GRANTHAM POLARITY SCORES
# Source: Siwek et al. 2025 / expasyProtScale
# ─────────────────────────────────────────────
AA_POLARITY = {
    'A': 8.1,  'R': 10.5, 'N': 11.6, 'D': 13.0, 'C': 5.5,
    'E': 12.3, 'Q': 10.5, 'G': 9.0,  'H': 10.4, 'I': 5.2,
    'L': 4.9,  'K': 11.3, 'M': 5.7,  'F': 5.2,  'P': 8.0,
    'S': 9.2,  'T': 8.6,  'W': 5.4,  'Y': 6.2,  'V': 5.9
}

# Chemistry classes (consistent with IBAM pipeline)
CHEMISTRY = {
    'K': 'BASIC',   'R': 'BASIC',   'H': 'BASIC',
    'D': 'ACIDIC',  'E': 'ACIDIC',
    'A': 'HYDRO',   'I': 'HYDRO',   'L': 'HYDRO',
    'M': 'HYDRO',   'F': 'AROM',    'W': 'AROM',
    'Y': 'AROM',    'V': 'HYDRO',   'P': 'HYDRO',
    'S': 'POLAR',   'T': 'POLAR',   'C': 'SPECIAL',
    'N': 'POLAR',   'Q': 'POLAR',   'G': 'SPECIAL'
}


def read_fasta(filepath):
    """Read multi- or single-sequence FASTA. Returns dict {header: sequence}."""
    sequences = {}
    current_header = None
    current_seq = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if current_header is not None:
                    sequences[current_header] = ''.join(current_seq)
                current_header = line[1:].strip()
                current_seq = []
            else:
                current_seq.append(line.upper())
    if current_header is not None:
        sequences[current_header] = ''.join(current_seq)
    return sequences


def polarity_diff(aa1, aa2):
    """Absolute rounded Grantham polarity difference. Returns None if AA unknown."""
    if aa1 not in AA_POLARITY or aa2 not in AA_POLARITY:
        return None
    return round(abs(AA_POLARITY[aa1] - AA_POLARITY[aa2]))


def gsima_position_mean(ibam_aa, myht_seq):
    """
    For a single IBAM residue, compute mean polarity difference against
    every valid position in MyhT. This is the per-taxon mean polarity-difference score for
    a given cassette position.
    Returns None if IBAM AA is unknown or no valid MyhT positions.
    """
    if ibam_aa not in AA_POLARITY or ibam_aa == '-':
        return None
    diffs = [polarity_diff(ibam_aa, aa) for aa in myht_seq if aa in AA_POLARITY]
    if not diffs:
        return None
    return np.mean(diffs)


def analyse_cassette(cassette_seqs, myht_seqs, shared_taxa):
    """
    For each cassette position (column), compute:
      - Per-taxon mean polarity-difference score
      - Cross-taxon mean and SD of those scores
      - Chemistry class consistency
    Returns list of dicts, one per cassette position.
    """
    # All cassette sequences should be same length
    lengths = [len(s) for s in cassette_seqs.values()]
    assert len(set(lengths)) == 1, "Cassette sequences differ in length — check for unfilled gaps"
    n_pos = lengths[0]

    results = []

    for pos in range(n_pos):
        taxon_scores = {}
        residues = {}

        for taxon in shared_taxa:
            cass = cassette_seqs[taxon]
            myht = myht_seqs[taxon]
            aa = cass[pos]
            if aa == '-':
                continue  # gap in alignment at this position for this taxon
            score = gsima_position_mean(aa, myht)
            if score is not None:
                taxon_scores[taxon] = score
                residues[taxon] = aa

        if len(taxon_scores) < 3:
            # Too few taxa to compute meaningful cross-taxon stats
            results.append({
                'pos': pos + 1,
                'n_taxa': len(taxon_scores),
                'cross_mean': None,
                'cross_std': None,
                'residues': residues,
                'chem_classes': {},
                'dom_class': None,
                'chem_pct': None,
                'skipped': True
            })
            continue

        scores = list(taxon_scores.values())
        res_list = list(residues.values())
        chem_classes = [CHEMISTRY.get(aa, '?') for aa in res_list]
        dom_class = max(set(chem_classes), key=chem_classes.count)
        dom_pct = chem_classes.count(dom_class) / len(chem_classes) * 100

        results.append({
            'pos': pos + 1,
            'n_taxa': len(taxon_scores),
            'cross_mean': np.mean(scores),
            'cross_std': np.std(scores),
            'residues': residues,
            'chem_classes': dict(zip(shared_taxa, chem_classes)),
            'dom_class': dom_class,
            'chem_pct': dom_pct,
            'skipped': False
        })

    return results


def print_report(results, cassette_seqs, shared_taxa):
    """Print the ranked GSIMA cross-taxon consistency report."""

    # Identify invariant positions (single unique residue across all taxa present)
    invariant = set()
    for r in results:
        if not r['skipped']:
            unique_res = set(r['residues'].values())
            if len(unique_res) == 1:
                invariant.add(r['pos'])

    print()
    print("=" * 78)
    print("GSIMA — IBAM MG CASSETTE n26 (60/90 dual-gate)")
    print("=" * 78)
    print(f"Taxa analysed: {len(shared_taxa)}")
    print(f"Cassette positions: {len(results)}")
    print(f"Invariant positions (single residue across all supporting taxa): "
          f"{len(invariant)} ({', '.join(str(p) for p in sorted(invariant))})")
    print()

    # Sort by cross-taxon std (ascending); skipped positions go last
    ranked = sorted(
        [r for r in results if not r['skipped']],
        key=lambda x: x['cross_std']
    )

    print("Positions ranked by GSIMA cross-taxon consistency (lowest std = most conserved):")
    print("-" * 78)
    print(f"{'Pos':>4} {'N':>4} {'X-Std':>7} {'X-Mean':>7} {'DomClass':>9} "
          f"{'Chem%':>6} {'Inv':>4}  Residues (first 8 taxa)")
    print("-" * 78)

    gsima_conserved = 0
    invariant_recovered = 0
    n_invariant = len(invariant)

    for r in ranked:
        is_inv = r['pos'] in invariant
        if r['cross_std'] < 0.5:
            gsima_conserved += 1
        if is_inv and r['cross_std'] < 0.5:
            invariant_recovered += 1

        inv_marker = " ***" if is_inv else "    "
        res_str = ','.join(list(r['residues'].values())[:8])
        if len(r['residues']) > 8:
            res_str += '...'
        print(f"{r['pos']:4d} {r['n_taxa']:4d} {r['cross_std']:7.3f} "
              f"{r['cross_mean']:7.2f} {r['dom_class']:>9} "
              f"{r['chem_pct']:5.1f}%{inv_marker}  {res_str}")

    # Skipped positions
    skipped = [r for r in results if r['skipped']]
    if skipped:
        print()
        print(f"Positions skipped (<3 taxa): "
              f"{', '.join(str(r['pos']) for r in skipped)}")

    print("-" * 78)
    print()
    print("VALIDATION SUMMARY")
    print(f"  GSIMA-conserved positions (cross-std < 0.5): {gsima_conserved} / {len(ranked)}")
    print(f"  Invariant positions recovered by GSIMA:       "
          f"{invariant_recovered} / {n_invariant}  "
          f"({'100%' if n_invariant and invariant_recovered == n_invariant else f'{invariant_recovered/n_invariant*100:.0f}%' if n_invariant else 'N/A'})")
    print()

    # Tryptophan spotlight
    trp_positions = [r for r in results if not r['skipped']
                     and any(aa == 'W' for aa in r['residues'].values())]
    if trp_positions:
        print("Tryptophan positions:")
        for r in trp_positions:
            n_trp = sum(1 for aa in r['residues'].values() if aa == 'W')
            print(f"  Pos {r['pos']:2d}: W in {n_trp}/{r['n_taxa']} taxa, "
                  f"cross-std = {r['cross_std']:.3f}, "
                  f"{'INVARIANT' if r['pos'] in invariant else 'variable'}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="GSIMA biochemical-convergence analysis of IBAM MG cassette (n26)"
    )
    parser.add_argument(
        '--cassette', required=True,
        help='FASTA file: MG_projected_trimmed_n26_core60_chem90.fa'
    )
    parser.add_argument(
        '--myht_dir', required=True,
        help='Directory containing MyhT FASTA files named <Taxon_name>_MyhT.fa'
    )
    parser.add_argument(
        '--std_threshold', type=float, default=0.5,
        help='Cross-taxon std threshold for GSIMA-conserved classification (default: 0.5)'
    )
    args = parser.parse_args()

    # ── Timestamp ───────────────────────────────────────────────────────────────
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    print(f"Run timestamp: {timestamp}")
    print()

    # ── Load cassette ──────────────────────────────────────────────────────────
    print(f"Loading cassette: {args.cassette}")
    cassette_seqs = read_fasta(args.cassette)
    print(f"  {len(cassette_seqs)} taxa loaded")

    # ── Load MyhT sequences ────────────────────────────────────────────────────
    myht_seqs = {}
    missing_myht = []
    for taxon in cassette_seqs:
        fname = os.path.join(args.myht_dir, f"{taxon}_MyhT.fa")
        if os.path.exists(fname):
            seqs = read_fasta(fname)
            # Take the first sequence in the file
            myht_seqs[taxon] = list(seqs.values())[0]
        else:
            missing_myht.append(taxon)

    if missing_myht:
        print(f"\nWARNING: No MyhT file found for {len(missing_myht)} taxa:")
        for t in missing_myht:
            print(f"  {t}  (expected: {t}_MyhT.fa)")
        print()

    shared_taxa = [t for t in cassette_seqs if t in myht_seqs]
    print(f"  MyhT sequences found for {len(shared_taxa)} / {len(cassette_seqs)} taxa")

    if len(shared_taxa) < 3:
        print("ERROR: Need at least 3 taxa with both cassette and MyhT sequences.")
        sys.exit(1)

    # ── Run analysis ───────────────────────────────────────────────────────────
    results = analyse_cassette(cassette_seqs, myht_seqs, shared_taxa)

    # ── Report ─────────────────────────────────────────────────────────────────
    print_report(results, cassette_seqs, shared_taxa)


if __name__ == '__main__':
    main()
