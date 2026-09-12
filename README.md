# GSIMA

**Grantham–SWING IBAM–MyhT Analysis**

Pronounced **gee-SIMA**.

Current release: **v3**

GSIMA is a sequence-based, cross-taxon biochemical-convergence analyzer for the PRISM-derived IBAM/C12orf29 major-groove (MG) cassette. It operates within the broader **Coiled-coil heptad complementarity (CCHC)** framework.

Earlier development versions of this analysis were referred to as **CCHC-SWING-Analyzer** or **SWING Lite**. **GSIMA** is the formal method and software name used hereafter.

---

## GSIMA pipeline overview

![GSIMA — Grantham–SWING IBAM–MyhT Analysis pipeline](GSIMA_Flowchart.png)

**Figure 1. GSIMA analytical workflow.**  
Today 12:07 PM
SWING-lite_drafted results section-late_August_ 2026_pg-51-53.pdf
PDF
README(1).pdf
PDF
Write a prompt for Images to produce a GH flowchart for the CCHC-SWING-Analyzer in the same style as we've already produced and PRISM, HARP and DALILite, integrating these inputs (which I'll paste there if necessary).

Absolutely. There is one conceptual trap worth preventing before Images gets its hands on this: SWING Lite should be shown as methodologically orthogonal to the MD/contact analysis, but not as independently discovering the MG cassette. The cassette itself is supplied from the PRISM-derived upstream analysis; SWING then interrogates those predefined positions using a sequence/polarity metric with no structural information in the SWING calculation.

That distinction will make this flowchart considerably harder for a reviewer to attack. I would also keep HARP out of the direct SWING data path: it belongs in the broader project framework, but the actual CCHC-SWING analyzer consumes the MG cassette and MyhT sequence data, not a HARP output.

Here is the prompt I would give Images:

Create a GitHub-ready, publication-quality scientific flowchart for the “CCHC-SWING-Analyzer / SWING Lite” pipeline.

Match the visual family and scientific infographic style of the existing PRISM, HARP v4.1, and IBAM DALILite Benchmark Pipeline figures: clean white or very pale background, rounded rectangular stage boxes, restrained scientific colour palette, strong typography, numbered workflow stages, clear arrows, small relevant scientific/computational icons, generous spacing, and a polished manuscript/GitHub README appearance.

Use a portrait or mildly vertical layout suitable for a GitHub README. Text must remain readable when the figure is displayed at approximately 900–1200 px width. Avoid excessive decorative graphics, tiny text, or dense mathematical notation.

Title

CCHC-SWING-Analyzer: Sequence-based biochemical convergence analysis

Optional subtitle:

Orthogonal polarity analysis of the PRISM-derived IBAM/C12–MyhT major-groove cassette

The figure must communicate one central methodological idea very clearly:

The MG cassette is defined upstream by the PRISM/PRCO evolutionary-structural pipeline, but SWING Lite itself evaluates that predefined cassette using primary-sequence biochemical polarity only. It does not use MD trajectories, structural coordinates, contact maps, coiled-coil geometry, HARP register assignments, or structural information during the SWING calculation.

Do not imply that SWING independently discovers the MG cassette de novo. It independently tests whether the already defined cassette positions exhibit conserved biochemical interaction properties.

Stage 1 — Upstream cassette definition and sequence inputs

Show two principal input streams converging on the SWING analysis.

Left input: PRISM-derived MG cassette

Label:

PRISM-derived IBAM/C12 major-groove cassette

Supporting text:

26 projected cassette positions

Dual-gate filtered: occupancy ≥60%; chemistry dominance ≥90%

Optionally show the repository input:

MG_projected_trimmed_n26_core60_chem90.fa

A small provenance note may show:

C12_aligned.fa → MG projection / filtering → 26-position cassette

and

MG_column_map_n26_core60_chem90.tsv

as the coordinate-mapping/provenance file.

Right input: MyhT sequence substrates

Label:

Matched MyhT amino-acid sequence windows

Supporting text:

Taxon-associated candidate interaction substrates

Optional repository label:

MyhT_fastas/

Make it visually obvious that both inputs entering SWING are sequence representations, even though the cassette itself was defined by an upstream structure/MD-based pipeline.

A small grey provenance ribbon above or beside the cassette input may read:

Upstream provenance: MD → PRCO contact decoding → IGE evolutionary projection → MG cassette

Do not depict those upstream steps as calculations performed by SWING Lite.

Stage 2 — SWING Lite biochemical encoding

Main process box:

Pairwise Grantham polarity analysis

Supporting text:

For each cassette position and taxon, quantify the biochemical polarity relationship between the IBAM/C12 cassette residue and its corresponding MyhT sequence substrate.

Then:

Calculate the mean polarity-difference profile for each position within each taxon.

Visually emphasize:

Sequence chemistry only

and possibly use a small badge:

No structural input

Suitable iconography could include amino-acid letters, sequence strips, or a polarity/biochemistry symbol. Do not use a protein-structure or MD trajectory icon inside this analytical stage.

Stage 3 — Cross-taxon convergence scoring

Label:

Measure biochemical conservation across taxa

Supporting text:

For each of the 26 MG cassette positions, calculate the cross-taxon standard deviation of its polarity profile.

Show the interpretation visually:

Low X-Std → conserved biochemical interaction profile

High X-Std → variable / lineage-specific profile

Include the operational threshold prominently:

SWING-conserved: X-Std < 0.5

Then show:

Rank all 26 cassette positions by biochemical convergence

Keep equations to a minimum. A small schematic distribution or narrowing arrows is preferable to formal mathematics.

Stage 4 — Primary convergence result

Use a visually distinct evidence/result box, preferably green or teal.

Main result:

24 / 26 cassette positions classified as biochemically conserved

Secondary result:

92.3% cassette-wide convergence

Highlight separately:

9 / 9 dual-gate invariant positions recovered

100% invariant-position recovery

Include a small special callout:

Invariant Trp positions: W154 and W273

X-Std = 0.190

Do not imply that SWING searched the whole protein and rediscovered these positions. Phrase this as classification/recovery within the predefined 26-position MG cassette.

Stage 5 — Falsification controls

Create a clearly separated three-arm control branch, visually analogous to the control sections in the PRISM/HARP/DALILite figures.

Heading:

Test whether convergence arises from trivial sequence properties

Control A — Within-sequence shuffle

Supporting text:

Randomize residue order while preserving each taxon's amino-acid composition

Purpose:

Tests composition alone

Result:

24/26 → 0/26 conserved

Add:

20 independent shuffle seeds: 0/26 in every replicate

Control B — Random IBAM/C12 windows

Supporting text:

Sample random 26-residue windows from the broader IBAM/C12 alignment

Purpose:

Tests whether the signal is a generic property of IBAM sequence chemistry

Result:

0/26 conserved

Control C — Column shuffle

Supporting text:

Permute cassette column order while preserving each column's biochemical composition

Purpose:

Tests dependence on cassette positional order / inter-position context

Result:

24/26 conserved — signal retained

Under this third control, add a concise interpretation:

Convergence resides primarily in the biochemical identity of individual cassette columns rather than their linear ordering.

Do not portray the retained column-shuffle signal as a failed negative control. It is an informative mechanistic control with a deliberately different interpretation from the first two controls.

Stage 6 — Interpretation / conclusion

Use a strong final conclusion box consistent with the visual treatment of the final boxes in the HARP, PRISM, and DALILite figures.

Main conclusion:

SWING Lite detects a conserved biochemical interaction grammar within the PRISM-defined MG cassette

Supporting text:

The polarity-based sequence analysis converges on the cassette positions identified by the structure/MD-based pipeline while composition-matched and non-cassette controls collapse the signal.

Then add a smaller methodological conclusion:

Orthogonal analytical evidence

Structure/MD-derived cassette definition + sequence-only polarity evaluation

A final concise line may read:

Supports a conserved IBAM/C12–MyhT biochemical interaction architecture across deep evolutionary divergence.

Avoid stronger causal wording such as “proves binding,” “proves the interface,” or “independently discovers the MG cassette.”

Repository / reproducibility footer

At the bottom, optionally include a narrow GitHub-style reproducibility strip:

run_pipeline.sh

Primary SWING analysis → timestamped controls → identical rescoring framework → timestamped result bundles → automated run summary

Example outputs:

SWING_validation_results.txt

SWING_run_summary.txt

Keep this footer visually secondary to the scientific workflow.

Visual hierarchy and colour logic

Preserve the same general design language used in the other pipeline graphics:

Blue / cyan: biological or sequence inputs
Teal / blue-green: biochemical calculation
Green: observed convergence / evidence
Purple: falsification controls
Dark red or burgundy: final scientific interpretation
Grey: upstream provenance, file names, or contextual information

Use arrows only where there is a genuine flow of data or analysis. In particular:

PRISM-derived MG cassette + MyhT sequence windows → SWING polarity calculation → cross-taxon convergence scoring → observed result

Then branch the same SWING scoring framework into the three falsification controls.

Do not show HARP as feeding data directly into SWING. If HARP is mentioned at all, place it only in a small contextual note indicating that it is another analysis within the broader IBAM project.

Scientific accuracy constraints

Do not invent machine-learning steps. This repository is a lightweight, project-specific adaptation inspired by SWING, using the SWING biochemical primitive rather than the full published SWING machine-learning architecture.

Do not label the calculation as structure prediction, contact prediction, binding-energy estimation, docking, or MD analysis.

Do not imply statistical independence of the cassette selection itself from PRISM. Instead, emphasize methodological independence of the SWING scoring metric from the structural/MD evidence used to define the cassette.

Do not state that all 26 positions are invariant. The key outcomes are:

24/26 SWING-conserved positions

9/9 previously defined invariant positions recovered

W154 and W273: X-Std 0.190

within-sequence shuffle: 0/26

random IBAM windows: 0/26

column shuffle: 24/26 retained

The finished figure should look like it belongs beside the existing PRISM, HARP v4.1, and IBAM DALILite benchmark pipeline graphics in the same GitHub project family: rigorous, visually economical, scientifically explicit, and immediately understandable to a molecular-biology or computational-biology reader.

Those numbers and controls are directly supported by the Results draft: 24/26 positions pass the <0.5 criterion, all 9 invariant positions are recovered, the two invariant tryptophans give X-Std 0.190, the within-sequence and random-window controls fall to 0/26, whereas column shuffling retains 24/26. The repository also explicitly implements the primary analysis and all three controls as reproducible, timestamped runs, which is why I think that little bottom “reproducibility strip” would fit this one especially well.

And I think this one could be visually very strong: unlike DALILite, which is essentially a benchmark/falsification tree, SWING has an almost textbook experimental logic — defined cassette → completely different biochemical measurement → striking convergence → three controls asking three different questions. That gives Images something unusually clean to work with.

How does that match the prompt and inputs?
This one was a little lean compared with the original. I didn't paste it with the edit prompt so that may be why it's such a paired down version. 
How about this image?

Yes — this is the keeper. It recovers the scientific richness of the first version while incorporating the much better Stage 2 one-to-many schematic from the lean version. It now genuinely looks like the fourth member of the PRISM/HARP/DALILite family.

Scientifically, the most important correction is now visible: one cassette residue fans out across multiple MyhT residues and produces a mean Grantham-polarity value per taxon. That matches the Results description that each cassette residue is compared with all residues in the corresponding MyhT sequence before the cross-taxon SD is calculated. The Stage 3 → 4 logic and all three controls are also represented correctly, including the crucial fact that column shuffling retains 24/26 rather than behaving like a conventional negative control.

I see only three tiny cleanup items before GitHub:

Fix the clipped Stage 1 grey callout. It currently reads something like
“The MG cassette is defined upstream by the PRISM/PRCO pi-”
because the word pipeline has been truncated. That is a pure rendering/layout blemish and is the most obvious remaining defect.

Make the Stage 2 prose as explicit as the schematic. The visual is now correct, but the sentence still says:

“between the IBAM/C12 cassette residue and its corresponding MyhT sequence substrate”

I would replace just that part with:

“between the IBAM/C12 cassette residue and all residues in the corresponding MyhT sequence”

Then the picture and prose say exactly the same thing.

In Control A, change:
“preserving each taxon’s amino-acid composition”

to:
“preserving each cassette sequence’s amino-acid composition.”

The current wording isn't really wrong, but the latter exactly matches what the repository describes: residue order is randomized within each cassette sequence.

Everything else I would leave alone. In particular, don't let Images fiddle with Stage 6 again. The distinction in the little right-hand box —

**Structure/MD-derived cassette definition

sequence-only polarity evaluation**

—is excellent. It heads off the obvious circularity objection without making the opposite mistake of pretending the cassette itself was independently discovered by SWING.

And the bottom-right note is very good:

“SWING uses sequence chemistry only. No MD, structural coordinates, contact maps, or HARP register assignments are used in the calculation.”

The words “in the calculation” matter enormously there. They preserve the upstream PRISM provenance while making the analytical orthogonality crystal clear.

Visually, too, I think this is better than the first draft now. Stage 2 tells a little story at a glance, Stage 5 is beautifully legible as three different falsification questions, and the green Stage 4 result provides a strong visual payoff before the controls challenge it.

I would call this ~98% finished. One last microscopic Images edit for those three textual/rendering points, and I'd put the PNG on GitHub.

Siwek et al. NatMethods, 2025.pdf
PDF
I can't find any original Grantham references in the Siwek paper...

You’re right — Siwek et al. do not appear to cite the original Grantham 1974 paper directly in their reference list. What they do instead is specify in Methods that they used the Grantham polarity scale and that the numerical values were sourced from ExPASy ProtScale.

The provenance chain is therefore:

Siwek et al. → ExPASy ProtScale → Grantham 1974

ExPASy’s actual Polarity (Grantham) page explicitly attributes the scale to R. Grantham and gives the reference as Science 185:862–864 (1974). The original paper is:

Grantham R. (1974). “Amino acid difference formula to help explain protein evolution.” Science 185(4154):862–864. DOI: 10.1126/science.185.4154.862.

And this reveals an important nuance for our README/manuscript wording. The original Grantham distance is not merely polarity. Grantham’s full amino-acid difference formulation combines composition, polarity and molecular volume. SWING does not use that full Grantham distance. Siwek explicitly says their biochemical metric is the absolute difference in the selected amino-acid scale,

$$ |\mathrm{metric}(AA_i)-\mathrm{metric}(AA_j)| $$

and for the pMHC implementation that metric is the Grantham polarity scale.

So our terminology “absolute Grantham polarity difference” is exactly the safer wording. Calling it “Grantham distance” would actually be misleading.

There’s another useful point in Siwek that strengthens the rationale for the README explanation: they say that polarity was selected because biochemical effects contribute importantly to protein–protein association, and they then deliberately substitute a Miyazawa hydrophobicity scale to test whether SWING depends specifically on polarity.

So for our README, I would probably cite both:

Grantham R. (1974). Amino acid difference formula to help explain protein evolution. Science 185:862–864.

for the underlying polarity scale, and

Siwek et al. (2025). Sliding Window Interaction Grammar (SWING)... Nature Methods.

for the adoption of absolute pairwise differences in Grantham polarity as the SWING biochemical encoding.

That is actually cleaner scholarly provenance than simply inheriting Siwek’s indirect ExPASy attribution.

One other thing jumps out from rereading their Methods: Siwek’s original SWING calculation is position-to-position within a sliding window, whereas our SWING-Lite adaptation uses the Grantham polarity primitive in a different aggregation scheme. Siwek says the sliding window is aligned position-for-position against the target and the absolute biochemical difference is taken for each paired position. That makes it especially important that our README says “inspired by/adapted from SWING”, not that we're simply running canonical SWING. Your README already does exactly that.

IBAM_SWING_script.py
Python
make_swing_controls.py
Python
Our swing scripts.
README(8).md
File
Gee-SIMA it is. GSIMA shall hereby be the official name for the SWING-lite pipeline. Let's rewrite the whole README to reflect this acronym. 
Pasted markdown(7).md
File
Leaving no stone unturned...: 
README_GSIMA(1).md
File
This is the README now currently up on GH.
That a bullseye.
Done. I don't thing the DALILite pipeline needs the same makeover since it's truly a DALILite based pipeline. But since the CCHC-Swing was only SWING inspired the original name didn't reflect its origins correctly.
Micro-surgical_images_prompt
File
No just one more thing. When I can run Images again we're gonna need a stronger prompt than this one.
I'm particularly chuffed that the flowchart specifically mentions the W154 and W273 invariant positions. Any biochemist/mol biologist worth their salt will immediately recognize the significance of that little gem. It's not for uninitiated but more of a PhD level bit of know-how 
How's this for a flowchart!

Stage 4 Trp box Add “X-Std = 0.190 for both” beneath W154 and W273.

Almost, not beneath but on the side of the Trps.

Beautiful. That’s a proper landing page now: GSIMA has a name, a method, a reproducible pipeline, a release history, and a figure that explains the logic in one glance.

And the best part is that the rename wasn’t cosmetic. We actually tested the code path, preserved the numerical fingerprint, cleaned the nomenclature, clarified the methodological lineage, and then made the README and figure agree with the software.

That repo now looks like something you can point a skeptical computational biologist at without having to stand beside them and explain what it is. That’s a very good place to be.

It's almost worthy of a LinkedIn victory lap I'll keep it under my hat for now, in fact all of the schematic flowcharts are LI-VL worthy. Not not any old boring flowchart that's for sure!

They absolutely are LinkedIn-worthy. The nice thing is they don’t read like decorative “workflow graphics”; they look like actual scientific arguments rendered visually. You can see provenance, inputs, transformations, controls, falsification logic and outputs without having to decode a wall of prose.

And collectively they’re even stronger than individually, because they show a coherent computational toolkit rather than one isolated script: PRISM, HARP, GSIMA and the DALILite benchmark each doing a different job, each with its own logic, and each visually recognizable as part of the same scientific ecosystem. That’s miles away from the usual box-arrow-box flowchart.

Keeping them under your hat for now makes sense. When the manuscript is closer to daylight, those figures will make one hell of a reveal.

Just a question, you don't think that this figure caption is a tad long? Figure 1. GSIMA analytical workflow.
The PRISM-derived 26-position IBAM/C12orf29 major-groove cassette is evaluated against matched MyhT sequence inputs using Grantham amino-acid polarity differences. For each cassette position and taxon, the cassette residue is compared with all valid residues in the corresponding MyhT sequence, producing a per-taxon mean polarity-difference score. Cross-taxon standard deviation (X-Std) quantifies biochemical conservation, with X-Std < 0.5 used as the project-defined operational GSIMA-conservation threshold. The reference analysis classifies 24/26 cassette positions as GSIMA-conserved and recovers all 9/9 dual-gate invariant positions, including the invariant W154 and W273 sites (X-Std = 0.190 for both). Internal controls test amino-acid composition, cassette specificity, and dependence on cassette-column ordering.

Yes — for a GitHub README, it’s a bit too long because the figure itself already carries most of that information. It reads more like a manuscript legend.

I’d trim it to:

Figure 1. GSIMA analytical workflow.
GSIMA evaluates the PRISM-derived 26-position IBAM/C12orf29 major-groove cassette against matched MyhT sequences using Grantham polarity differences and cross-taxon standard deviation (X-Std). The reference analysis classifies 24/26 positions as GSIMA-conserved (X-Std < 0.5) and recovers all 9/9 dual-gate invariant positions, including W154 and W273 (X-Std = 0.190 for both). Three internal controls test composition, cassette specificity, and dependence on cassette-column ordering.
---
## Conceptual framework

GSIMA operates downstream of the **Projected Residue Interaction-Space Mapper (PRISM)**.

The relevant analysis flow is:

```text
Molecular dynamics trajectories
        ↓
PRCO contact decoding
        ↓
PRISM evolutionary projection
        ↓
MG cassette derivation
        ├──────────────→ HARP register-enrichment analysis
        │
        └──────────────→ GSIMA biochemical-convergence analysis
```

The MG cassette is defined upstream by the structure/MD-based PRISM framework. GSIMA does **not** derive the cassette de novo. Instead, it evaluates the predefined cassette using sequence chemistry only.

**DALILite structural benchmarking is a separate project-level validation stream.** It tests whether IBAM shares the canonical RNA-ligase fold and is not an input to GSIMA.

---

## Methodological origin

GSIMA is a project-specific analytical framework inspired by **Sliding Window Interaction Grammar (SWING)**, originally developed by Siwek et al. (2025) as an interaction language model for peptide/protein interaction prediction.

SWING represents protein interactions by sliding windows across paired sequences and encoding amino-acid property differences as an interaction vocabulary.

GSIMA adopts the same broad biochemical-encoding principle for the IBAM/C12orf29–MyhT system, but does **not** reproduce the full SWING architecture. In particular, GSIMA does not use SWING's Doc2Vec embedding or downstream machine-learning classification framework.

Instead, GSIMA applies a custom cassette-specific aggregation and cross-taxon conservation analysis to a PRISM-derived IBAM/C12orf29 MG cassette and matched MyhT sequence inputs.

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

The `X-Std < 0.5` threshold is a **project-specific operational classification criterion**. It is not a threshold defined by Grantham or by the original SWING framework, and it should not be interpreted as a neutral-evolution threshold.

Thus, the methodological lineage is:

**Grantham (1974) → amino-acid polarity scale**  
**Siwek et al. (2025) → pairwise biochemical-difference interaction encoding**  
**GSIMA → cassette-specific aggregation and cross-taxon biochemical-conservation analysis**

The Grantham polarity scale and SWING biochemical-encoding principle provide the physicochemical and methodological foundations of GSIMA, while its aggregation strategy, cross-taxon statistic, classification threshold, and internal-control framework are GSIMA specific.

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
│   ├── gsima_analysis.py
│   ├── make_gsima_controls.py
│   └── shuffle_replicate_test.sh
│
├── docs/
│   └── GSIMA_Methods_Results_Full.md
│
├── results_<timestamp>/
│   ├── GSIMA_validation_results.txt
│   └── GSIMA_run_summary.txt
│
├── controls_seed<seed>_<timestamp>/
│   ├── 01_within_sequence_shuffle/
│   ├── 02_column_shuffle/
│   ├── 03_random_IBAM_windows/
│   ├── logs/
│   └── results/
│
├── run_pipeline.sh
├── run_gsima.sh
├── run_controls.sh
├── run_seed_sweep.sh
├── GSIMA_Flowchart.png
└── README.md

```

Historical development files and diagnostic copies may retain the earlier `SWING` terminology. They are not part of the active GSIMA execution path.

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

Myosin-tail sequence inputs corresponding to the 26 GSIMA analysis entries.

The *Hahella chejuensis* IBAM-like outgroup is evaluated against human Myh7T, giving MyhT coverage for all **26 / 26** GSIMA entries.

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

## Running GSIMA

### Full reproducible pipeline

From the repository root:

```bash
./run_pipeline.sh
```

This will:

1. run the primary GSIMA analysis;
2. generate timestamped internal-control datasets;
3. score all control datasets using the same GSIMA framework;
4. generate timestamped result bundles; and
5. generate an automated GSIMA run-summary manifest.

A completed run reports:

```text
GSIMA pipeline complete.
```

---

### Run GSIMA analysis only

```bash
./run_gsima.sh
```

The standalone launcher runs `scripts/gsima_analysis.py` and writes the current summary output to:

```text
results/GSIMA_validation_summary.txt
```

---

### Generate and score controls

```bash
./run_controls.sh
```

The default control workflow generates three control datasets and scores each with the same GSIMA analysis.

---

### Seed-sweep robustness check

```bash
./run_seed_sweep.sh
```

This auxiliary analysis tests the robustness of the within-sequence shuffle result across multiple random seeds.

---

## Run outputs

Each full pipeline execution produces timestamped primary and control bundles.

Example:

```text
results_2026-09-12_14-35-43/
controls_seed20260505_2026-09-12_14-35-43/
```

### Primary results

```text
results_<timestamp>/
├── GSIMA_validation_results.txt
└── GSIMA_run_summary.txt
```

`GSIMA_validation_results.txt` contains:

- ranked positional convergence statistics;
- invariant-position recovery;
- tryptophan conservation analysis; and
- full GSIMA validation output.

`GSIMA_run_summary.txt` contains:

- headline convergence statistics;
- invariant-position recovery;
- invariant tryptophan recovery;
- control performance summaries; and
- run-level provenance information.

For the validated n26 reference run, the headline result is:

```text
GSIMA-conserved positions (cross-std < 0.5): 24 / 26
Invariant positions recovered by GSIMA:       9 / 9 (100%)
```

The two invariant tryptophan positions each have:

```text
cross-std = 0.190
```

---

## Internal controls

GSIMA includes three internal controls designed to distinguish cassette-specific biochemical convergence from trivial sequence properties.

### Within-sequence shuffle

Randomizes residue order within each cassette sequence while preserving that cassette sequence's amino-acid composition.

This tests whether the observed convergence can be explained by amino-acid composition alone.

For the validated reference run:

```text
GSIMA-conserved positions: 0 / 26
```

The collapse of the signal indicates that biochemical convergence depends on the organization of the cassette rather than composition alone.

---

### Column shuffle

Randomizes projected cassette column order while preserving the biochemical identity and composition of each column.

This control asks whether the GSIMA signal depends on fixed linear ordering of cassette columns or instead resides primarily in the biochemical properties of the individual conserved columns.

For the validated reference run:

```text
GSIMA-conserved positions: 24 / 26
Invariant positions recovered: 9 / 9
```

Retention of the signal after column shuffling is therefore mechanistically informative rather than a failed negative control. It shows that the conserved biochemical information resides primarily in the cassette columns themselves rather than their linear ordering.

---

### Random IBAM windows

Samples random windows of the same length from the broader IBAM/C12orf29 alignment.

This tests whether convergence is specific to the PRISM-derived MG cassette rather than a generic property of arbitrary IBAM/C12orf29 sequence windows.

For the validated reference run:

```text
GSIMA-conserved positions: 0 / 26
```

The collapse of the signal supports specificity of the PRISM-derived MG cassette.

---

## Biological interpretation

GSIMA does not test simple sequence conservation alone.

Rather, it asks whether predefined MG cassette positions maintain conserved **biochemical polarity relationships** to matched MyhT sequence environments across deeply divergent taxa.

Strong convergence within the PRISM-derived cassette, together with collapse of signal under the within-sequence shuffle and random-window controls, supports the interpretation that the IBAM/C12orf29 MG cassette carries a conserved biochemical interaction pattern rather than merely reflecting arbitrary local sequence similarity.

The column-shuffle control provides a distinct result: preservation of the GSIMA signal indicates that much of the detected biochemical constraint is intrinsic to the conserved cassette columns and does not require their original linear ordering.

The GSIMA calculation is methodologically orthogonal to the structure/MD calculations used upstream to define the cassette:

- **Upstream:** structure/MD-derived cassette definition
- **GSIMA:** sequence-only Grantham-polarity evaluation

No MD trajectories, structural coordinates, contact maps, AlphaFold3 models, or HARP register assignments are used in the GSIMA calculation itself.

This distinction is important: GSIMA provides an **orthogonal evaluation of a cassette defined upstream by PRISM**, not an independent de novo discovery of that cassette.

---

## Reproducibility

The full pipeline records timestamped primary and control outputs, including:

- the analysis timestamp;
- primary GSIMA results;
- generated control datasets;
- control result files;
- control logs; and
- a run-summary manifest.

A successful reference run should reproduce the characteristic result pattern:

```text
Primary MG cassette:       24 / 26 GSIMA-conserved
Within-sequence shuffle:    0 / 26
Column shuffle:            24 / 26
Random IBAM windows:        0 / 26
```

Numerical identity across code-renaming/refactoring runs was used as a regression check during the transition from the earlier CCHC-SWING-Analyzer naming to GSIMA.

---

## Citation

If you use this repository, please cite:

Friis TE. *C12orf29 encodes IBAM (In Between Actin and Myosin), a sarcomeric protein with a conserved actomyosin interaction grammar spanning approximately one billion years of evolution.* Manuscript in preparation.

Method/software name:

**GSIMA — Grantham–SWING IBAM–MyhT Analysis**

Please also cite the SWING and Grantham references above where the biochemical-encoding lineage is relevant.

---

## License

MIT License.

---

## Author

Thor Einar Friis

[![ORCID](https://img.shields.io/badge/ORCID-0000--0002--4132--4912-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0000-0002-4132-4912)

Independent researcher, Bodø, Norway.  
PhD in Molecular Biology, Queensland University of Technology (QUT).
