# GSIMA

**Grantham–SWING IBAM–MyhT Analysis**

Pronounced **gee-SIMA**.

Current release: v2

GSIMA is a sequence-based, cross-taxon biochemical-convergence analyzer for the PRISM-derived IBAM/C12orf29 major-groove (MG) cassette. It operates within the broader **Coiled-coil heptad complementarity (CCHC)** framework.

Earlier development versions of this analysis were referred to as **CCHC-SWING-Analyzer** or **SWING Lite**. **GSIMA** is the formal method name used hereafter.

---

## Conceptual framework

GSIMA operates downstream of the **Projected Residue Interaction-Space Mapper (PRISM)**.

The broader analytical framework proceeds as:

```text
Molecular dynamics trajectories
        ↓
PRCO contact decoding
        ↓
PRISM evolutionary projection
        ↓
MG cassette derivation
        ↓
HARP register enrichment analysis
        ↓
GSIMA biochemical-convergence analysis
        ↓
DALILite structural falsification
```

The MG cassette is defined upstream by the structure/MD-based PRISM framework. GSIMA does **not** derive the cassette de novo. Instead, it evaluates the predefined cassette using sequence chemistry only.

---

## Methodological origin

GSIMA is a project-specific analytical framework inspired by **Sliding Window Interaction Grammar (SWING)**, originally developed by Siwek et al. (2025) as an interaction language model for peptide/protein interaction prediction.

SWING represents protein interactions by sliding windows across paired sequences and encoding amino-acid property differences as an interaction vocabulary.

GSIMA adopts the same broad biochemical-encoding principle for the IBAM/C12orf29–MyhT system, but does not reproduce the full SWING architecture. In particular, GSIMA does **not** use SWING's Doc2Vec embedding or downstream machine-learning classification framework.

Instead, GSIMA applies a custom cassette-specific aggregation and cross-taxon conservation analysis to a PRISM-derived IBAM/C12orf29 MG cassette and matched MyhT sequence windows.

### Biochemical metric

GSIMA uses the **Grantham amino-acid polarity scale** (Grantham, 1974) as its biochemical metric.

For an amino-acid pair, the biochemical encoding is the absolute difference between their Grantham polarity values:

```text
ΔP = round(|P(IBAM aa) - P(MyhT aa)|)
```

where `P` denotes the Grantham polarity value.

This follows the biochemical-encoding principle used by Siwek et al. (2025), in which interacting amino-acid pairs are represented by absolute differences in a selected biochemical property.

The original SWING framework generates these pairwise encodings by positionally aligning a sliding window against a target sequence and subsequently incorporating the resulting interaction language into an embedding/classification pipeline.

GSIMA adopts only the **pairwise biochemical-difference principle**. Its downstream analytical logic is specific to this project:

1. For each IBAM/C12orf29 MG cassette position and each taxon, the cassette residue is compared against **all valid residues in the corresponding MyhT sequence**.
2. The resulting absolute Grantham polarity differences are averaged to produce a **per-taxon mean polarity-difference score** for that cassette position.
3. These per-taxon means are compared across taxa.
4. The **cross-taxon standard deviation (X-Std)** is used as the measure of biochemical conservation.
5. Positions with **X-Std < 0.5** are classified operationally as **GSIMA-conserved**.

Low X-Std indicates that a cassette position maintains a similar biochemical relationship to its MyhT sequence environment across divergent taxa. High X-Std indicates greater biochemical variability.

The `X-Std < 0.5` threshold is a **project-specific classification criterion**; it is not a threshold defined by Grantham or by the original SWING framework.

Thus, the methodological lineage is:

**Grantham (1974) → amino-acid polarity scale**  
**Siwek et al. (2025) → pairwise biochemical-difference interaction encoding**  
**GSIMA → cassette-specific aggregation and cross-taxon biochemical-conservation analysis**

The Grantham polarity scale and SWING biochemical-encoding principle provide the physicochemical and methodological foundations of GSIMA, while its aggregation strategy, cross-taxon statistic, classification threshold, and falsification framework are specific to GSIMA.

### SWING citation

Siwek, J. C., Omelchenko, A. A., Chhibbar, P., et al. (2025).  
*Sliding Window Interaction Grammar (SWING): a generalized interaction language model for peptide and protein interactions.*  
**Nature Methods**, 22, 1707–1719.  
https://doi.org/10.1038/s41592-025-02723-1

### Grantham polarity scale

Grantham, R. (1974).  
*Amino acid difference formula to help explain protein evolution.*  
**Science**, 185(4154), 862–864.  
https://doi.org/10.1126/science.185.4154.862

---

## Repository structure

```text
GSIMA/
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

### Legacy filenames

Several v2 script, launcher, and output filenames retain the earlier `SWING` terminology for compatibility and reproducibility, including `IBAM_SWING_script.py`, `run_swing.sh`, `SWING_validation_results.txt`, and `SWING_run_summary.txt`.

These historical filenames do **not** indicate that GSIMA runs the full SWING machine-learning model.

---

## Input files

### `C12_aligned.fa`

Source evolutionary alignment used to derive the MG-projected cassette representation analysed by GSIMA.

Included for provenance and reproducibility.

---

### `MG_column_map_n26_core60_chem90.tsv`

Mapping table linking projected MG positions to source alignment coordinates.

---

### `MG_projected_trimmed_n26_core60_chem90.fa`

Final MG-projected cassette used for GSIMA analysis.

Represents the conserved IBAM/C12orf29 MG interaction cassette after dual-gate filtering:

- occupancy threshold ≥ 60%
- chemistry dominance threshold ≥ 90%

---

### `MyhT_fastas/`

Myosin-tail FASTA windows spanning 25 taxa. The *Hahella chejuensis* IBAM-like outgroup is evaluated against human Myh7T.

These sequences represent the candidate MyhT interaction substrates evaluated against the conserved MG cassette.

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

1. Run the primary GSIMA analysis
2. Generate timestamped internal control datasets
3. Score all control datasets using the same GSIMA framework
4. Generate timestamped results bundles
5. Generate an automated run-summary manifest

---

### Run GSIMA only

The v2 launcher retains its historical filename:

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

## Primary results

```bash
results_<timestamp>/
├── SWING_validation_results.txt
└── SWING_run_summary.txt
```

`SWING_validation_results.txt` contains:

- ranked positional convergence statistics
- invariant-position recovery
- tryptophan conservation analysis
- full validation output

`SWING_run_summary.txt` contains:

- headline convergence statistics
- invariant-position recovery
- invariant tryptophan recovery
- control performance summaries
- run-level provenance information

The `SWING_` prefix is retained in v2 output filenames for backward compatibility; the analytical framework represented by these outputs is GSIMA.

---

## Internal controls

GSIMA includes three falsification controls designed to distinguish cassette-specific biochemical convergence from trivial sequence properties.

### Within-sequence shuffle

Randomizes residue order within each cassette sequence while preserving its amino-acid composition.

Tests whether the observed convergence can be explained by cassette amino-acid composition alone.

#### Expected outcome

Loss of convergence signal.

---

### Column shuffle

Randomizes projected cassette column order while preserving the biochemical identity and composition of each column.

This control tests whether GSIMA signal depends on fixed linear ordering of cassette columns or instead resides primarily in the biochemical properties of the individual conserved columns.

Retention of substantial signal after column shuffling is therefore mechanistically informative rather than a failed negative control.

---

### Random IBAM windows

Samples random windows of the same length from the broader IBAM/C12orf29 alignment.

Tests whether convergence is specific to the PRISM-derived MG cassette rather than a generic property of arbitrary IBAM/C12orf29 sequence windows.

#### Expected outcome

Collapse of convergence signal.

---

## Biological interpretation

GSIMA does not test simple sequence conservation alone.

Rather, it asks whether predefined MG cassette positions maintain conserved **biochemical polarity relationships** to matched MyhT sequence environments across deeply divergent taxa.

Strong convergence within the PRISM-derived cassette, together with collapse of signal under composition-preserving and non-cassette controls, supports the interpretation that the IBAM/C12orf29 MG cassette encodes a conserved biochemical interaction architecture rather than arbitrary local sequence similarity.

The analytical evidence is methodologically orthogonal to the structure/MD calculations used upstream to define the cassette:

- **Upstream:** structure/MD-derived cassette definition
- **GSIMA:** sequence-only Grantham-polarity evaluation

No MD trajectories, structural coordinates, contact maps, AlphaFold3 models, or HARP register assignments are used in the GSIMA calculation itself.

---

## Citation

If you use this repository, please cite:

Friis TE. *C12orf29 encodes IBAM (In Between Actin and Myosin), a sarcomeric protein with a conserved actomyosin interaction grammar spanning approximately one billion years of evolution.* Manuscript in preparation.

Method/software name:

**GSIMA — Grantham–SWING IBAM–MyhT Analysis**

---

## License

MIT License.

---

## Author

Thor Einar Friis

[![ORCID](https://img.shields.io/badge/ORCID-0000--0002--4132--4912-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0000-0002-4132-4912)

Independent researcher, Bodø, Norway.  
PhD in Molecular Biology, Queensland University of Technology (QUT).
