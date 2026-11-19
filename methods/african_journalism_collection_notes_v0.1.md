# African journalism discovery audit — v0.1 (2026-11-18)

## Scope and relationship to the project
This register is the **African-origin subset of the third corpus (journalistic coverage)**. It does **not** create a fourth corpus. The first two corpora remain (1) Rwanda and DR Congo government communication and (2) European football-club communication. The journalism corpus also has an international-press stratum (Europe and the United States), added on 2026-11-18: [34 candidate records](../data/international_journalism_discovery_v0.1.csv), documented in the [international press protocol](international_press_visibility_protocol_v0.1.md).

- Data: [37 candidate records](../data/african_journalistic_coverage_discovery_v0.1.csv)
- Geography, based on publication outlet: Rwanda (8), DR Congo (15), and other African / pan-African outlets (14).
- Records are bibliographic discoveries; **not 37 included analytical observations**.
- Main event-matched comparison: 2025–2026; pre-2025 reports serve historical context, where eligible.
- Original URLs and titles only, no copyrighted article text reproduced.

## Search pathway
Purposeful web-domain searches of The New Times, Actualite.cd, 7SUR7.CD, Radio Okapi, The EastAfrican, Africanews, Citizen Digital, and Daily Monitor. Queries crossed Rwanda/RDC/DRC with Arsenal, Paris Saint-Germain, Bayern Munich, Atlético Madrid, Aston Villa, AS Monaco, FC Barcelona, and AC Milan, using English and French terms (partenariat, sponsoring, Visit Rwanda, RDC Cœur de l’Afrique). This is **not** a systematic crawl or a complete outlet census.

## Event matching and sampling
- RWA-ARSENAL-LAUNCH-2018 and RWA-PSG-LAUNCH-2019: historical context.
- RWA-SPONSORSHIP-CRITICISM-2025: DRC diplomatic appeals to European clubs, February 2025.
- RWA-PSG-RENEW-2025 and RWA-ATLETI-LAUNCH-2025: sponsorship extensions/new deal.
- RWA-BAYERN-RESTRUCTURE-2025: shift from commercial tourism branding to football development.
- RWA-ARSENAL-END-2025: November 2025 announcement of partnership conclusion June 2026.
- RWA-VILLA-LAUNCH-2026: candidate event outside original six-club discovery inventory; cross-check inclusion rules and add the club to the club corpus if retained.
- DRC-MONACO-LAUNCH-2025, DRC-MONACO-MILAN-LAUNCH-2025, DRC-BARCA-LAUNCH-2025: launch and contract announcements.
- DRC-SPENDING-DEBATE-2025/2026: political and economic accountability reactions, including Congolese domestic sport priorities.
- DRC-MONACO-ACCOUNTABILITY-2026 and DRC-IMPLEMENTATION-2026: allegations, official responses, and implementation delays.

## Critical integrity flags
1. **Outlet location is not article origin**: Reuters, AFP, or other syndicated stories reproduced by Kenyan/Ugandan outlets cannot be treated as independent local reporting without checking bylines and source credits. Some rows are explicitly marked `wire_republication_review`.
2. **Genre variation**: Radio Okapi's dialogue programme and Actualite.cd's signed opinion/tribune should be retained only under predeclared genre rules and analyzed separately from straight news.
3. **Dates**: Partial dates (YYYY or YYYY-MM) are intentionally recorded at their known precision. Complete day-level dates must be independently recovered before event-window coding.
4. **Title integrity**: Some lengthy titles are abbreviated in the discovery register. Recheck originals before publication-grade export.
5. **Sampling asymmetry**: 8/15/14 is a discovery count, not comparative output, newsroom salience or national preference. Search intensities and indexed availability differ.
6. **Claims require attribution**: sponsorship values, impact, official denials, alleged misconduct, and responsibility for conflict are claims reported by particular speakers, not author-verified facts.
7. **Ownership and independence**: confirm outlets' location, publisher, byline, and actual reporting source. Avoid automatically describing a publication as independent.
8. **AC Milan gap**: The DRC source material reports AC Milan involvement. Existing club-communication discovery includes Monaco and Barcelona; search for Milan's own original club announcement before event comparison.
9. **Aston Villa gap**: A 2026 Rwanda sponsorship story surfaced. Verify date and revise the six-club boundary consistently or treat as documented out-of-scope material.
10. **International journalism (updated 2026-11-19)**: An African-only register does not satisfy the proposal's European-press component. A discovery register for the international press now exists (34 candidates: UK 10, France 10, USA 6, Italy 4, Germany 3, Spain 1). It is unverified and uncoded, and it has not yet been matched event by event against this register.

## Pending work before 'collection complete' can be claimed
- Independently open each candidate URL and verify exact title, date, journalist/byline, source agency, genre, country of original production, and relevance.
- Deduplicate aliases, mirrored pages, translations, syndicated newswire versions, and updates; preserve one master record with secondary publication links.
- Screen within predeclared event windows and scope. Record exclusion reasons; avoid adjusting sample solely to balance case numbers.
- Search missing reporting by Congolese, Rwandan, and regional outlets with multilingual synonyms and event-specific dates. Log positive and negative searches.
- Match the international-press register (started 2026-11-18) against the same event list, and align event keys across the two press registers. Check original club reports for AC Milan (and Aston Villa if included).
- Freeze a versioned screened sample, then pilot code and test reliability before treating narrative patterns as findings.

## Preliminary patterns: interpret as hypotheses only
- In the sampled Rwanda-based reporting, sponsorship often appears through visibility, tourism, sporting opportunity and talent development.
- In sampled DRC-based reporting, costs, legitimacy, accountability and implementation feature prominently.
- Regional African outlets include both commercial and geopolitical interpretations; wire dependency must be measured rather than assumed.
These are **search-stage observations**, not coded results or claims of national media consensus.
