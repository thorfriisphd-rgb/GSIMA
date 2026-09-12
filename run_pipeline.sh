#!/usr/bin/env bash
set -euo pipefail

TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
RESULTS_DIR="results_${TIMESTAMP}"
SUMMARY_FILE="${RESULTS_DIR}/GSIMA_run_summary.txt"

mkdir -p "${RESULTS_DIR}"

echo "====================================="
echo "GSIMA — Grantham–SWING IBAM–MyhT Analysis"
echo "====================================="

echo
echo "[1/2] Running GSIMA analysis..."

python scripts/gsima_analysis.py \
    --cassette data/MG_projected_trimmed_n26_core60_chem90.fa \
    --myht_dir data/MyhT_fastas \
    | tee "${RESULTS_DIR}/GSIMA_validation_results.txt"

echo
echo "Primary GSIMA results:"
echo "  ${RESULTS_DIR}"


echo
echo "[2/2] Running GSIMA controls..."

./run_controls.sh


GSIMA_RESULTS="${RESULTS_DIR}/GSIMA_validation_results.txt"

GSIMA_CONSERVED_LINE=$(grep "GSIMA-conserved positions" "${GSIMA_RESULTS}" || true)
INVARIANT_RECOVERED_LINE=$(grep "Invariant positions recovered" "${GSIMA_RESULTS}" || true)
TRP_LINES=$(grep "^  Pos .*W in .*INVARIANT" "${GSIMA_RESULTS}" || true)

CONTROL_DIR=$(ls -td controls_* | head -n 1)

WITHIN_RESULTS="${CONTROL_DIR}/results/within_sequence_shuffle_results.txt"
COLUMN_RESULTS="${CONTROL_DIR}/results/column_shuffle_results.txt"
RANDOM_RESULTS="${CONTROL_DIR}/results/random_window_results.txt"

WITHIN_GSIMA=$(grep "GSIMA-conserved positions" "${WITHIN_RESULTS}" || true)
WITHIN_INV=$(grep "Invariant positions recovered" "${WITHIN_RESULTS}" || true)

COLUMN_GSIMA=$(grep "GSIMA-conserved positions" "${COLUMN_RESULTS}" || true)
COLUMN_INV=$(grep "Invariant positions recovered" "${COLUMN_RESULTS}" || true)

RANDOM_GSIMA=$(grep "GSIMA-conserved positions" "${RANDOM_RESULTS}" || true)
RANDOM_INV=$(grep "Invariant positions recovered" "${RANDOM_RESULTS}" || true)


cat > "${SUMMARY_FILE}" << EOF
==================================================
GSIMA — Grantham–SWING IBAM–MyhT Analysis — Run Summary
==================================================

Run timestamp:
  ${TIMESTAMP}

Primary results directory:
  ${RESULTS_DIR}

Control results directory:
  $(ls -td controls_* | head -n 1)

Main cassette:
  data/MG_projected_trimmed_n26_core60_chem90.fa

Key findings:
  ${GSIMA_CONSERVED_LINE}
  ${INVARIANT_RECOVERED_LINE}

Invariant tryptophan positions:
${TRP_LINES}

Control headline results:

Within-sequence shuffle:
  ${WITHIN_GSIMA}
  ${WITHIN_INV}

Column shuffle:
  ${COLUMN_GSIMA}
  ${COLUMN_INV}

Random IBAM windows:
  ${RANDOM_GSIMA}
  ${RANDOM_INV}

Controls generated:
  - Within-sequence shuffle
  - Column shuffle
  - Random IBAM windows

Pipeline status:
  COMPLETE

EOF

echo
echo "Run summary written to:"
echo "  ${SUMMARY_FILE}"



echo
echo "====================================="
echo "GSIMA pipeline complete."
echo "====================================="
