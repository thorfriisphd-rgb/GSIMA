#!/usr/bin/env bash
set -euo pipefail

mkdir -p results

python scripts/gsima_analysis.py \
    --cassette data/MG_projected_trimmed_n26_core60_chem90.fa \
    --myht_dir data/MyhT_fastas \
    | tee results/GSIMA_validation_summary.txt
