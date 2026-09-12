#!/usr/bin/env bash
set -euo pipefail

echo "[1/4] Generating internal control FASTAs..."
python scripts/make_gsima_controls.py

# Detect newest timestamped controls directory
CONTROL_DIR=$(ls -td controls_* | head -n 1)

mkdir -p "${CONTROL_DIR}/results"
mkdir -p "${CONTROL_DIR}/logs"

echo
echo "Using control directory:"
echo "  ${CONTROL_DIR}"

echo
echo "[2/4] Scoring within-sequence shuffle control..."
python scripts/gsima_analysis.py \
    --cassette "${CONTROL_DIR}/01_within_sequence_shuffle/MG_n26_within_sequence_shuffled.fa" \
    --myht_dir data/MyhT_fastas \
    | tee "${CONTROL_DIR}/results/within_sequence_shuffle_results.txt"

echo
echo "[3/4] Scoring column shuffle control..."
python scripts/gsima_analysis.py \
    --cassette "${CONTROL_DIR}/02_column_shuffle/MG_n26_column_shuffled.fa" \
    --myht_dir data/MyhT_fastas \
    | tee "${CONTROL_DIR}/results/column_shuffle_results.txt"

echo
echo "[4/4] Scoring random-window control..."
python scripts/gsima_analysis.py \
    --cassette "${CONTROL_DIR}/03_random_IBAM_windows/C12_random_windows_n26.fa" \
    --myht_dir data/MyhT_fastas \
    | tee "${CONTROL_DIR}/results/random_window_results.txt"

echo
echo "GSIMA control analysis complete."
echo "Results written to:"
echo "  ${CONTROL_DIR}/results"
