#!/usr/bin/env bash
# Multi-seed sweep for the within-sequence shuffle control.
# Purpose: check whether the reported 0/26 GSIMA-conserved result at
# seed=20260505 is representative, or an artifact of a single draw.
#
# Usage:
#   ./run_seed_sweep.sh [n_seeds] [myht_dir]
#
# Produces one controls_seed<N>_<timestamp>/ folder per seed, and a
# summary TSV (sweep_summary.tsv) tabulating GSIMA-conserved counts.

set -euo pipefail

N_SEEDS="${1:-20}"
MYHT_DIR="${2:-data/MyhT_fastas}"
SUMMARY="sweep_summary.tsv"

# Run from repo root: scripts reference data/ paths relative to cwd.

echo -e "seed\tgsima_conserved\tinvariant_recovered\tn_invariant\tcontrol_dir" > "$SUMMARY"

for seed in $(seq 1 "$N_SEEDS"); do
    echo "=== Seed $seed ==="

    python3 scripts/make_gsima_controls.py --seed "$seed"

    # Most recent matching folder for this seed
    ctrl_dir=$(ls -dt controls_seed${seed}_* | head -n 1)

    out=$(python3 scripts/gsima_analysis.py \
        --cassette "${ctrl_dir}/01_within_sequence_shuffle/MG_n26_within_sequence_shuffled.fa" \
        --myht_dir "$MYHT_DIR")

    echo "$out"

    gsima_conserved=$(echo "$out" | grep "GSIMA-conserved positions" | grep -oP '\d+(?= /)')
    denom=$(echo "$out" | grep "GSIMA-conserved positions" | grep -oP '(?<=/ )\d+')
    invariant_recovered=$(echo "$out" | grep "Invariant positions recovered" | grep -oP '\d+(?= /)')
    n_invariant=$(echo "$out" | grep "Invariant positions recovered" | grep -oP '(?<=/ )\d+')

    echo -e "${seed}\t${gsima_conserved}/${denom}\t${invariant_recovered}\t${n_invariant}\t${ctrl_dir}" >> "$SUMMARY"
done

echo
echo "Sweep complete. Summary written to $SUMMARY"
column -t "$SUMMARY"
