#!/usr/bin/env python3
import random
import argparse
from pathlib import Path
from datetime import datetime

parser = argparse.ArgumentParser(
    description="Generate SWING falsification controls (within-sequence shuffle, "
                 "column shuffle, random C12 windows) for the IBAM MG n26 cassette."
)
parser.add_argument(
    "--seed", type=int, default=20260505,
    help="Random seed for all three shuffle/sampling controls (default: 20260505, "
         "matching the locked-in manuscript run)."
)
args = parser.parse_args()

ROOT = Path.cwd()
MG = Path("data/MG_projected_trimmed_n26_core60_chem90.fa")
C12 = Path("data/C12_aligned.fa")
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
OUT = ROOT / f"controls_seed{args.seed}_{timestamp}"

random.seed(args.seed)

print(f"Run timestamp: {timestamp}")
print(f"Seed: {args.seed}")
print()

# Create standard subfolders
(OUT / "logs").mkdir(parents=True, exist_ok=True)
(OUT / "results").mkdir(parents=True, exist_ok=True)

def read_fasta(path):
    records = []
    name, seq = None, []
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            if name:
                records.append((name, "".join(seq)))
            name, seq = line, []
        else:
            seq.append(line)
    if name:
        records.append((name, "".join(seq)))
    return records

def write_fasta(records, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    if isinstance(records, dict):
        iterable = records.items()
    else:
        iterable = records

    with open(path, "w") as f:
        for name, seq in iterable:
            name = str(name).lstrip(">").strip()
            f.write(f">{name}\n{seq}\n")

mg = read_fasta(MG)
c12 = read_fasta(C12)

# 1. Within-sequence shuffle: preserves each taxon's cassette composition.
#    NOTE: operates on the already dual-gate-filtered, position-fixed n26
#    cassette — i.e. downstream of column/position selection, per taxon
#    independently. This is what makes it a valid null: it destroys each
#    taxon's residue-to-position mapping without touching the upstream
#    position-selection step.
within = []
for name, seq in mg:
    chars = list(seq)
    random.shuffle(chars)
    within.append((name, "".join(chars)))

write_fasta(
    within,
    OUT / "01_within_sequence_shuffle" / "MG_n26_within_sequence_shuffled.fa"
)

# 2. Column shuffle: preserves column identities but randomizes cassette order/register
seqs = [seq for _, seq in mg]
names = [name for name, _ in mg]
L = len(seqs[0])
order = list(range(L))
random.shuffle(order)

column_shuffled = []
for name, seq in mg:
    column_shuffled.append((
        name,
        "".join(seq[i] for i in order)
    ))

write_fasta(
    column_shuffled,
    OUT / "02_column_shuffle" / "MG_n26_column_shuffled.fa"
)

(OUT / "02_column_shuffle" / "column_shuffle_order.tsv").write_text(
    "new_position\told_position\n" +
    "\n".join(f"{new+1}\t{old+1}" for new, old in enumerate(order)) +
    "\n"
)

# 3. Random same-length C12 windows: same length as MG cassette
# Removes gaps; samples one 26-aa window per taxon where possible.
random_windows = []
for name, seq in c12:
    ungapped = seq.replace("-", "").replace(".", "")
    if len(ungapped) < L:
        continue
    start = random.randint(0, len(ungapped) - L)
    window = ungapped[start:start+L]
    random_windows.append((
        name,
        window
    ))

write_fasta(
    random_windows,
    OUT / "03_random_IBAM_windows" / "C12_random_windows_n26.fa"
)

print("Wrote controls:")
print(f"  {OUT}/01_within_sequence_shuffle/MG_n26_within_sequence_shuffled.fa")
print(f"  {OUT}/02_column_shuffle/MG_n26_column_shuffled.fa")
print(f"  {OUT}/03_random_IBAM_windows/C12_random_windows_n26.fa")
print(f"Results folder: {OUT}/results")
print(f"Logs folder:    {OUT}/logs")
print("Column shuffle order saved.")
