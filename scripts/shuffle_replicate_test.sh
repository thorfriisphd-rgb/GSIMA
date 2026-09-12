#!/usr/bin/env bash
# shuffle_replicate_test.sh
#
# Runs the SWING within-sequence shuffle control N times (with different
# seeds where possible) and tabulates the resulting distribution of
# GSIMA-conserved position counts (out of 26).
#
# Purpose: find out (a) whether the 0/26 vs 1/26 discrepancy reflects
# genuine run-to-run stochasticity in an unseeded shuffle, and more
# importantly (b) whether the real, unshuffled 24/26 result sits far
# outside the full range this null distribution ever produces.
#
# I don't have your actual GSIMA CLI syntax or MyhT sequence data,
# so the CONFIG block below is a template — the exact command and the
# output-parsing pattern are placeholders. Edit them to match your real
# invocation before running.

set -euo pipefail

# ---------------------- CONFIG (edit this block) ----------------------
N_REPS="${1:-100}"                                   # number of replicate runs

GSIMA_CMD="python3 gsima_analysis.py"                    # <-- EDIT: real script/path
CASSETTE="data/MG_projected_trimmed_n26_core60_chem90.fa"   # <-- EDIT if path differs
SHUFFLE_FLAG="--shuffle within_sequence"             # <-- EDIT: real flag/value

# If your script doesn't accept an explicit seed, delete the next line
# and the "$SEED_FLAG" "$seed" arguments in the loop below — repeated
# calls will then just use whatever unseeded randomness the script
# already has, which is fine for building the distribution.
SEED_FLAG="--seed"                                   # <-- EDIT or remove

OUTDIR="shuffle_replicates_$(date +%Y%m%d_%H%M%S)"
SUMMARY="${OUTDIR}/summary.tsv"
# ------------------------------------------------------------------------

mkdir -p "$OUTDIR"
echo -e "replicate\tseed\tconserved_count" > "$SUMMARY"

echo "Running $N_REPS replicates of the within-sequence shuffle control..."
echo ""

for i in $(seq 1 "$N_REPS"); do
    seed=$i
    outfile="${OUTDIR}/rep_${i}.txt"

    # EDIT: adjust this call to match your actual GSIMA CLI
    if ! $GSIMA_CMD --cassette "$CASSETTE" $SHUFFLE_FLAG "$SEED_FLAG" "$seed" > "$outfile" 2>&1; then
        echo "  rep $i: FAILED (see $outfile)"
        echo -e "${i}\t${seed}\tFAILED" >> "$SUMMARY"
        continue
    fi

    # EDIT: adjust this pattern to match your actual output line, e.g.:
    #   "Within-sequence shuffle: GSIMA-conserved positions (cross-std < 0.5): 0 / 26"
    count=$(grep -oP 'conserved positions.*?:\s*\K[0-9]+' "$outfile" || echo "NA")

    echo -e "${i}\t${seed}\t${count}" >> "$SUMMARY"
    printf "  rep %3d  seed %3d  conserved=%s\n" "$i" "$seed" "$count"
done

echo ""
echo "=================================================================="
echo " Distribution across $N_REPS replicates"
echo "=================================================================="
awk -F'\t' 'NR>1 && $3 != "FAILED" {print $3}' "$SUMMARY" | sort -n | uniq -c | \
    awk -v n="$N_REPS" '{printf "  conserved=%-4s  count=%-4s  (%.1f%%)\n", $2, $1, $1/n*100}'

echo ""
awk -F'\t' 'NR>1 && $3 != "NA" && $3 != "FAILED" {
    sum+=$3; n++
    if (min=="" || $3<min) min=$3
    if ($3>max) max=$3
} END {
    if (n==0) { print "No valid results parsed — check the grep pattern against your actual output format."; exit }
    printf "n=%d valid runs   min=%s   max=%s   mean=%.2f\n", n, min, max, sum/n
}' "$SUMMARY"

echo ""
echo "Individual replicate outputs saved in: $OUTDIR/"
echo "Full tabulation:                        $SUMMARY"
echo ""
echo "Next step: compare the max value above against the REAL, unshuffled"
echo "result (24/26). If 24 sits far above anything this null distribution"
echo "produces, that confirms the control is doing its job — it's the"
echo "result you want, not a discrepancy to resolve."
echo ""
echo "Separately, and just as important: run the REAL (unshuffled)"
echo "analysis twice and diff the output. That call has no randomization"
echo "in it at all, so it should be byte-identical every time. If it"
echo "isn't, that's a determinism bug in the core pipeline, distinct from"
echo "anything the shuffle control is testing."
