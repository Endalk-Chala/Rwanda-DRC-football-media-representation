# Rwanda–DR Congo: Football Sponsorship and Media Representation

**Discovery-stage release. Study period: 2018-01-01 to 2026-11-13. Registers last updated: 2026-11-18.**

This repository documents the source discovery for a comparative study of Rwanda's and DR Congo's sponsorship partnerships with European football clubs. It covers three corpora: government communications, European club communications, and journalism (African and international press).

**All records are candidates found through targeted searches. Verification is partial, screening is not done, and nothing has been coded.** The counts below describe what the searches found. They are not measures of media attention, tone, or representativeness, and they should not be compared across the two countries as evidence.

## Research question

How do Rwanda and DR Congo construct state narratives through European football partnerships, and how do European clubs and news organizations in Africa, Europe, and the United States relay, qualify, or contest those narratives?

## Study design

The study has three empirical corpora:

1. **Government communications** from Rwandan and Congolese state institutions.
2. **European football club communications** from the partner clubs.
3. **Journalism**, in two strata: African press and international press.

Commercial arrangements and political economy are analytic dimensions across these corpora. They are not a fourth corpus.

## Data inventory

| Corpus | File | Candidate records | Breakdown | Collected |
|---|---|---|---|---|
| 1. Government | [government_source_register.csv](data/government_source_register.csv) | 39 | Rwanda 30, DR Congo 9 | 2026-11-13 |
| 2. Clubs | [club_communications_discovery_v0.1.csv](data/club_communications_discovery_v0.1.csv) | 19 | Rwanda partners 14, DR Congo partners 5 | 2026-11-17 |
| 3a. African press | [african_journalistic_coverage_discovery_v0.1.csv](data/african_journalistic_coverage_discovery_v0.1.csv) | 37 | Rwanda-based 8, DR Congo-based 15, other African and pan-African 14 | 2026-11-18 |
| 3b. International press | [international_journalism_discovery_v0.1.csv](data/international_journalism_discovery_v0.1.csv) | 34 | UK 10, France 10, USA 6, Italy 4, Germany 3, Spain 1 | 2026-11-18 |
| **Total** | | **129** | | |

Supporting files:

- [verification_audit_v0.3.csv](data/verification_audit_v0.3.csv): page-level audit of 22 government records.
- [supplementary_official_reports_and_boundary_sources.csv](data/supplementary_official_reports_and_boundary_sources.csv): 9 resources kept apart from the corpora (5 Rwanda Development Board annual reports, 2 campaign-website items, 1 football federation statement, 1 state news agency item). These are not coded observations.
- [claim_register_template.csv](data/claim_register_template.csv): an empty template for logging and checking reported claims such as reach, spending, and tourism figures.

### Corpus 1: Government communications

- 39 candidate documents, dated 2018-05-23 to 2026-05-08, in English (29) and French (10).
- Sources are official domains, mainly `rdb.rw` and `sports.gouv.cd`.
- Partner clubs named: Arsenal, Paris Saint-Germain, Bayern Munich, Atlético de Madrid, AS Monaco, FC Barcelona, and AC Milan.
- 22 records have had their page content inspected. The other 17 await an independent page-level check.

### Corpus 2: European club communications

- 19 candidate records from six clubs: FC Bayern (5), Paris Saint-Germain (4), Atlético de Madrid (3), AS Monaco (3), Arsenal (2), and FC Barcelona (2).
- Dated records run from 2023-08-27 to 2026-09-07. Six records have no confirmed publication date (3 undated pages, 3 awaiting a date check).
- Genres include press releases, club news, statements, partner pages, a fans' forum document, a video, and a photo gallery. The video is not transcribed and the images are not coded.
- 13 records are core candidates; the other 6 are contextual or companion material.
- No AC Milan club communication has been located yet.

### Corpus 3a: African press

- 37 candidate items from eight outlets: The New Times (8), 7SUR7.CD (8), The EastAfrican (8), Actualite.cd (6), Daily Monitor (3), Citizen Digital (2), Radio Okapi (1), and Africanews (1).
- Publication dates run from 2018 to 2026. Thirteen records carry only a month or a year and need day-level dates before event-window coding.
- Items are linked to 17 event keys, such as the February 2025 Congolese appeal to European clubs, the November 2025 Arsenal announcement, and the Congolese spending debate.
- Outlet location is not article origin: 5 records are flagged as possible wire or syndicated copy, and originality has not been checked for the other 32.
- No page has been audited and no record has been screened.

### Corpus 3b: International press

- 34 candidate items from 13 publishers, including The Guardian, BBC Sport, Le Monde, L'Équipe, Calcio e Finanza, La Gazzetta dello Sport, Deutsche Welle, El País, The Athletic, The Washington Post, Reuters, and the Financial Times.
- Case focus: Rwanda 21, DR Congo 6, both 7.
- Publication dates run from 2018-05-29 to 2026-11-17. Four records carry only a month.
- 22 records are core candidates. The rest are historical context (6), context only (4), one opinion candidate, and one wire master copy.
- Records were confirmed through search results. Full article text has not been uniformly checked, and genre and frame are not coded.

## Time boundary and comparison

- **Empirical evidence:** 2018-01-01 to 2026-11-13.
- **Before 2018:** literature and historical context only.
- **Comparability:** Rwanda's partnerships began in 2018 and DR Congo's in 2024 to 2025. The study examines development within each case over time and compares the two cases in common event windows in 2024 to 2026. Cumulative raw counts are not compared across unequal sponsorship histories.

## Status and known limits

- **Discovery method.** All registers come from targeted domain and multilingual web searches. None is a full archive crawl or a complete census of an outlet.
- **Verification.** An inspected page is not an approved analytic record. Titles, dates, bylines, genre, and origin still need checking for most records.
- **Possible duplicate.** GOV-RWA-030, a French-language Paris Saint-Germain renewal release, may duplicate the English release and should not be counted twice.
- **Wire and syndicated copy.** Reuters, AFP, and AP stories republished by other outlets must be identified and linked to one master record.
- **AC Milan.** Government and press records refer to an AC Milan agreement and to a reported payment dispute, but the club corpus has no AC Milan record. Disputed assertions are to be attributed to their sources, not treated as established.
- **Aston Villa.** One African press record (NEWS-028) concerns a 2026 Aston Villa candidate event outside the original club list. An inclusion decision is pending.
- **Record after the cutoff.** INTPRESS-032 is dated 2026-11-17, after the 2026-11-13 study cutoff. It needs an inclusion decision.
- **Non-coverage.** No register yet records searches that returned nothing. An outlet-by-event search matrix is planned so that "not found after a documented search" can be distinguished from "never published."
- **Reported impact figures.** Reach, engagement, spending, and tourism numbers are claims made by their sources, not independently established effects.
- **No findings.** The repository contains no coded narrative observations and no intercoder reliability results. Patterns described in the notes are working hypotheses.

## Methods and documentation

- [Search and screening protocol](methods/search_protocol.md) (government corpus)
- [African journalism collection notes](methods/african_journalism_collection_notes_v0.1.md)
- [International press visibility and sampling protocol](methods/international_press_visibility_protocol_v0.1.md)
- [Decision log](methods/decisions.md)
- [Provisional codebook](codebook/codebook_v0.1.md) (drafted for the government corpus; a shared codebook for the press corpora is planned)
- Research reflections: [November 17](notes/research_reflection_2026-11-17.md) and [November 18](notes/research_reflection_2026-11-18.md). These record emerging questions, not coded findings.

## Validation

Run `python scripts/validate.py` to check field structure in every register: unique IDs and URLs, HTTPS links, date formats, allowed codes, agreement between the government register and its audit file, and URLs repeated across registers. It reports errors, which must be fixed, and warnings, which need a decision. The script does not open any URL, and it does not test whether sources are valid, live, or complete.

As of 2026-11-19 it reports no errors and six warnings: five paired-record references in the club register that use an ID format (`RWA-CLUB-004`) different from the file's record IDs (`CLUB-004`), and the post-cutoff date of INTPRESS-032. It also lists 18 event keys that appear in only one of the two press registers, which will need aligning before event-matched comparison.

## Next steps

1. Verify each candidate: exact title, date, byline, language, genre, origin, and relevance.
2. Remove duplicates and link wire reproductions and translations to a master record.
3. Record screening decisions and exclusion reasons.
4. Fix common event windows and build the outlet-by-event search matrix, including searches with no results.
5. Pilot a shared codebook across the three corpora and test intercoder reliability.

## Reuse and licensing

The repository publishes original URLs, bibliographic metadata, and reproducibility materials only. It does not reproduce third-party article texts or images. Code is under the MIT License ([LICENSE_CODE.txt](LICENSE_CODE.txt)). Researcher-authored metadata and documentation are intended for CC BY 4.0 on final publication ([LICENSE_METADATA.txt](LICENSE_METADATA.txt)). Linked sources remain under their original rights. A data DOI and a formal version tag may be added once screening and metadata checks are complete.

## Author

Endalkachew H. Chala
