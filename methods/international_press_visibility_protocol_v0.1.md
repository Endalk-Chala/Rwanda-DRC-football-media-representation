# International press extension and visibility testing — 2026-11-18

## Status and dataset
[International journalistic discovery register](../data/international_journalism_discovery_v0.1.csv) holds **34 candidate records**: UK 10, France 10, Italy 4, Germany 3, Spain 1, USA 6. It is an extension **within corpus C: journalism**, not a new corpus. Geographic label means publisher's home-market/affiliation and **not** necessarily the reporter's location or source of reporting.

As with the [African press discovery register](../data/african_journalistic_coverage_discovery_v0.1.csv), counts reflect **purposeful search discovery**, not population estimates or measured outlet output. Some records are historical/contextual, opinion, syndications, and undated-to-day items. The Athletic is a New York Times Company publication, not the New York Times newsroom. Washington Post articles may be wire copy; bylines/source credits must be checked. Financial Times is contextual as titled. Search access to NYT primary pages was restricted; Athletic references are provisional until primary confirmation. Preserve missing/partial date precision.

## Research question and conceptual caution
**RQ extension:** Under what circumstances do European football sponsorships generate favorable, neutral, critical, or no identifiable *earned-news* coverage, and how does this differ between Rwanda and DR Congo, events, countries, and news outlets?

- **Purchased brand exposure** (shirt, stadium ads, broadcasts, partnerships) is not the same thing as **earned journalism** (newsroom editorial mentions). Governments can achieve commercial visibility despite negative press and vice versa.
- **Quantity** (number or share of news pieces) is distinct from **valence** (tone) and from **narrative uptake** (whether tourism/development branding is repeated, attributed, problematized, or rejected).
- **No coverage observed in a sampled newspaper** is not proof of no coverage or campaign failure; audit each outlet systematically with exact search protocol and indicate indexing/paywall limits.
- No claims of return on investment, tourism arrivals causation, ad reach, or reduced foreign visibility should be made without independently measured outcomes.
- Critical accountability journalism is not a priori discrediting of an African state; compare institutions and voices symmetrically.

## Screening and reproducible measures
Before claiming relative exposure, establish the outlet-by-event observation matrix with all target outlets including **explicit zero cells** when identical search protocols were completed.
Recommended outlet strata: UK (Guardian, BBC), France (Le Monde, L'Équipe), Italy (Gazzetta, Calcio e Finanza, optionally Corriere), Germany (DW), Spain (El País), US (NYT newsroom, Athletic separately, WaPo). Distinguish AP/Reuters/AFP master copy from local reprints.

For each club/government paired event:
1. Freeze publication windows (e.g. first 7 days post-announcement; ±30 days around controversy; special event-based longer windows predeclared). Use matched windows for both cases. Historical 2018–2024 sources are a separately identified contextual stratum.
2. Log multilingual Boolean queries, domain, collection time, result count, manual site-search results and restrictions; supplement with licensed news databases (Factiva, Nexis, ProQuest) or archives where available for completeness.
3. Independently open article, verify date/byline/genre/article origin and exact title, deduplicate syndications/updates/translation variants and assign inclusion reasons.
4. Code **journalistic newsworthiness** (article centers partnership vs brief mention), **sponsor visibility** (headline/lead/body/incident), **narrative use** (tourism, investment, talent development, culture, conflict, accountability), **evaluation** (positive/mixed/neutral/critical with transparent code rules and intercoder reliability), **quote and source origin** (government/club/critics/experts/affected communities), and **brand treatment** (reproduced, juxtaposed, challenged).
5. Compute per-event, per-outlet **count**, share of candidate coverage, prominence, and within-item share of attributable brand narrative. Report by strata and provide uncertainty and search coverage documentation.
6. Where no matching coverage appears, label as `not_found_after_documented_search` rather than definite absence. Compare outcomes with sponsor intent **claimed in official corpus**; do not automatically infer that the objective was favorable news coverage.
7. Conduct negative-case checks: some foreign press discusses sport-related success or tourism favorably (e.g. German DW and certain Le Monde pieces), while other pieces emphasize conflict, contracts, fan opposition, or alleged missed payments. Record framing after reading/coding, not based on title alone.

## Prominent discoveries and interpretation to verify
- **UK:** The Guardian and BBC Sport Africa report both the deals and disputes, including the February 2025 DRC appeal and November 2025 Arsenal ending announcement.
- **France:** Le Monde and L'Équipe report both countries, multiple club agreements, tourism/soft-power aspirations, and criticism.
- **Italy:** Calcio e Finanza has 2025–2026 DRC-AC Milan contract-payment disputes and a reported subsequent termination; investigate legal and financial evidence and compare against primary club/state claims before accepting allegations as independently confirmed.
- **Germany:** DW follows FC Bayern's shift away from commercial sponsorship to academy development.
- **US:** The Athletic, linked through NYT, covers Arsenal. Washington Post publishes related opinion and incidental material, but wires/originality and scope require auditing. Do not claim comprehensive NYT newsroom absence.

## Important manuscript claim
Suggested cautious formulation: *European club sponsorship purchases branded placement, but does not buy control of independent journalistic interpretation. Event-matched comparisons can reveal how earned coverage amplifies, ignores, or contests sponsors' intended country narratives.* This is a hypothesis/design objective until coding and counts are complete.

## Next actions
- Finish source-level audits and bylines, particularly NYT/Athletic access and WaPo wires, publication dates and French/Italian translation checks.
- Expand Italian independent press, French press, Spanish Atlético-specific coverage, and US international outlets via licensed archive access.
- Resolve boundary of AC Milan and Aston Villa in club corpus.
- Create outlet-by-event search log and zero-cell coverage matrix; do not select only events that yielded stories.
- Sample and code African and international press under the **same** protocol; pre-register or version-frame definition and reliability test.
