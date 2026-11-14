# Rwanda–DR Congo: Football Sponsorship and Media Representation

**Stage 1 discovery release v0.3.0 — collection cutoff: 2026-11-13**

This repository transparently documents a government-source discovery round for the comparative study of Rwanda and DR Congo European football sponsorship messaging. **Discovery collection is complete for this version; exhaustive coverage, source screening, and coding are not.** Claims about population representativeness are explicitly withheld.

## Data inventory
- **39 candidate government documents** (30 Rwanda, 9 DR Congo) in [data/government_source_register.csv](data/government_source_register.csv), from 2018 through November 13, 2026.
- **22 records with on-page content inspected** in [data/verification_audit_v0.3.csv](data/verification_audit_v0.3.csv). The other **17 await independent page-level checking**.
- **9 supplemental institutional/report resources** in [data/supplementary_official_reports_and_boundary_sources.csv](data/supplementary_official_reports_and_boundary_sources.csv): 5 RDB annual reports, plus 4 separately categorized campaign/federation/state-news items. These are **not** additional coded observations.
- **No formally coded narrative observations or reliability results**, and no third-party full texts reproduced.

## Time boundary and comparison
- **Empirical evidence:** 2018-01-01 through 2026-11-13.
- **Before 2018:** literature/historical context only, not an empirical observation.
- **Comparability:** Rwanda's partnerships predate DRC's. Examine within-case temporal development and compare common event windows in 2024–2026; avoid comparing cumulative raw counts for unequal sponsorship histories.

## Audit and data-quality limits
The research register was assembled via targeted official-domain and multilingual web searches, *not* a fully enumerated archive crawl. An inspected page is not the same as an approved analytic sample. A French version of a PSG announcement (GOV-RWA-030) may duplicate the English release and must be resolved before analysis. Boundary records whose titles mention sport but not European football sponsorship need screening. Original reported impact metrics are source claims, not independently established effects.

## Key files
- [Search and screening protocol](methods/search_protocol.md)
- [Decision log](methods/decisions.md)
- [Verification audit](data/verification_audit_v0.3.csv)
- [Codebook (provisional)](codebook/codebook_v0.1.md)
- [Claim-verification template](data/claim_register_template.csv)
- [Validation script](scripts/validate.py)

Run `python scripts/validate.py` to check machine-readable field structure; **this does not test source validity or completeness**.

## Reuse
Publish original URLs, bibliographic metadata, coding, and reproducibility materials only. Do not republish copyrighted content or pictures without permissions. Repository data DOI pending. Formal version tag/DOI may be added once screening and metadata QA are complete.

## Research question
How do Rwanda and DR Congo construct competing state narratives through European football partnerships, and how are these narratives mediated or contested by European clubs and journalism?
