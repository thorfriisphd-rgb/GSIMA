
# CCHC-SWING-Analyzer
Current release: v2

---

## Conceptual framework

CCHC-SWING-analyzer operates downstream of the IBAM Grammar Engine (IGE).

The broader analytical framework proceeds as:

```text
Molecular dynamics trajectories
        ↓
PRCO contact decoding
        ↓
IGE evolutionary projection
        ↓
MG cassette derivation
        ↓
HARP register enrichment analysis
        ↓
SWING cassette-convergence analysis
        ↓
DALILite structural falsification
```

---

## Methodological origin

This repository implements a project-specific, lightweight adaptation inspired by Sliding Window Interaction Grammar (SWING), originally developed as an interaction language model for peptide/protein interaction prediction.

SWING represents protein interactions by sliding windows across paired sequences and encoding amino-acid property differences as an interaction vocabulary.

In this repository, the same broad conceptual principle is adapted to the IBAM/C12orf29 system: an IBAM-Grammar-Engine-derived major-groove cassette is compared against conserved MyhT sequence windows to test cassette-level interaction-grammar convergence.

This implementation is not a re-release of the original SWING model. It is a simplified, project-specific analytical adaptation for CCMHCG/C12–MyhT interaction-grammar testing.

### SWING citation

Siwek, J. C., Omelchenko, A. A., Chhibbar, P., et al. (2025).
*Sliding Window Interaction Grammar (SWING): a generalized interaction language model for peptide and protein interactions.*
Nature Methods.

---

## Repository structure

```text
CCHC_SWING_analyzer/
│
├── data/
│   ├── C12_aligned.fa
│   ├── MG_column_map_n26_core60_chem90.tsv
│   ├── MG_projected_trimmed_n26_core60_chem90.fa
│   └── MyhT_fastas/
│
├── scripts/
│   ├── IBAM_SWING_script.py
│   └── make_swing_controls.py
│
├── docs/
│
├── results_<timestamp>/
│   ├── SWING_validation_results.txt
│   └── SWING_run_summary.txt
│
├── controls_<timestamp>/
│   ├── 01_within_sequence_shuffle/
│   ├── 02_column_shuffle/
│   ├── 03_random_IBAM_windows/
│   ├── logs/
│   └── results/
│
├── run_pipeline.sh
├── run_swing.sh
├── run_controls.sh
│
└── README.md
```

---

## Input files

### `C12_aligned.fa`

Source evolutionary alignment used to derive the MG-projected cassette representation employed by SWING Lite.

Included for provenance and reproducibility.

---

### `MG_column_map_n26_core60_chem90.tsv`

Mapping table linking projected MG positions to source alignment coordinates.

---

### `MG_projected_trimmed_n26_core60_chem90.fa`

Final MG-projected cassette used for SWING analysis.

Represents the conserved CCMHCG/C12 interaction core after dual-gate filtering:

- occupancy threshold => 60%
- chemistry dominance threshold => 90%

---

### `MyhT_fastas/`

Myosin-tail FASTA windows spanning 25 taxa. The *Hahella chejuensis* IBAM-like outgroup interacts with human Myh7T.

These represent the candidate interaction substrates evaluated against the conserved MG cassette.

---

## Installation

Tested on:

- Ubuntu Linux
- Python 3.10+

Install dependencies as required:

```bash
pip install numpy pandas biopython
```

---

## Running the pipeline

### Full reproducible run

From repository root:

```bash
./run_pipeline.sh
```

This will:

1. Run primary SWING Lite analysis
2. Generate timestamped internal control datasets
3. Score all control datasets using the same SWING framework
4. Generate timestamped results bundles
5. Generate an automated run-summary manifest

---

### Run SWING only

```bash
./run_swing.sh
```

---

### Generate controls only

```bash
./run_controls.sh
```

---

### Run outputs

Each execution produces timestamped result bundles.

Example:

```bash
results_2026-05-10_10-49-52/
controls_2026-05-10_10-49-52/
```
---

---
## Primary results

```bash
results_<timestamp>/
├── SWING_validation_results.txt
└── SWING_run_summary.txt
```


SWING_validation_results.txt contains:

ranked positional convergence statistics,
invariant-position recovery,
tryptophan conservation analysis,
and full validation output.

SWING_run_summary.txt contains:

headline convergence statistics,
invariant-position recovery,
invariant tryptophan recovery,
control performance summaries,
and run-level provenance information.

---
### Control bundles

```bash
controls_<timestamp>/
├── 01_within_sequence_shuffle/
├── 02_column_shuffle/
├── 03_random_IBAM_windows/
├── logs/
└── results/
```
Each bundle contains:

generated control FASTA datasets, corresponding SWING result summaries, logs, and audit-traceable outputs.

This structure was designed to support transparent and fully reproducible computational analysis.

---
## Internal controls
### Within-sequence shuffle

Randomizes residue order within each cassette sequence while preserving amino-acid composition.
Tests whether convergence depends on positional biochemical organization rather than residue frequency alone.
#### Expected outcome
loss of convergence signal.

### Column shuffle

Randomizes projected cassette column order while preserving column composition.

This control tests whether SWING signal derives primarily from conserved biochemical column identities rather than fixed positional ordering within the cassette.

Observed behavior indicates that substantial signal is retained when conserved biochemical columns are preserved.


### Random IBAM windows

Samples random windows from the broader IBAM/C12 alignment.

Tests whether convergence is specific to the projected MG cassette rather than a generic property of arbitrary sequence windows.

Expected outcome
collapse of convergence signal.

---
## Biological interpretation

SWING does not test simple sequence conservation alone.

Rather, it evaluates whether projected MG cassette positions exhibit conserved biochemical interaction grammar across deeply divergent MyhT substrates.

Strong convergence in the projected cassette, combined with collapse of signal under randomized controls, supports the interpretation that the CCHC/IBAM MG cassette encodes a conserved biochemical interaction architecture rather than arbitrary local sequence similarity.

---

## Citation

If you use this repository, please cite:

Friis TE. *C12orf29 encodes IBAM (In Between Actin and Myosin), a sarcomeric protein with a conserved actomyosin interaction grammar spanning approximately one billion years of evolution.* Manuscript in preparation.

---
## License

MIT License.

---

## Author

Thor Einar Friis

[![ORCID](https://img.shields.io/badge/ORCID-0000--0002--4132--4912-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0000-0002-4132-4912)

Independent researcher, Bodø, Norway.
PhD in Molecular Biology, Queensland University of Technology (QUT).

