# Codebook v0.3

**Status:** revised after the pilot of 2026-11-19. Ten documents were coded with v0.2; the problems found are listed in section 12 and are addressed here. The pilot documents have been recoded with this version.
**Replaces:** [codebook_v0.2.md](codebook_v0.2.md).
**Covers:** all three corpora: government communications, European club communications, and journalism (African and international press).

## 1. Purpose

The codebook supports one comparative question: how do Rwanda and DR Congo present their partnerships with European football clubs, how do the clubs present them, and how do news organizations in Africa, Europe, and the United States relay, qualify, or contest those presentations?

The variables record what a text says. They do not record whether a campaign worked, and no variable should be read as a measure of effect.

## 2. Unit of analysis

One unit is one distinct document: a government web page or official minute, a club page or document, or a news item.

- A translation or language version of a document already in the corpus is linked to its master record and coded once (example: GOV-RWA-030 is coded under GOV-RWA-007).
- A wire story republished by another outlet is coded once, under the wire master record. The republication is logged, not coded again.
- For long documents that address the partnership in one part only (council minutes, a fans' forum record, a season review), the unit is the passage about the partnership. Record its location in `evidence_note`, and judge centrality within the passage.

## 3. Eligibility

Code a document only if it meets both conditions:

1. It was published between 2018-01-01 and 2026-11-13.
2. It does one of the following:
   - it refers to a partnership, sponsorship, or cooperation between Rwanda or DR Congo (the state, a state agency, or the national tourism brand) and a European football club; or
   - it is a government or club document that uses a partner club, its current or former players, its staff, its stadium, or its supporters to present the country, even if the partnership is not named.

A news item that names a club without referring to the partnership is not eligible. Record it as `excluded_no_partnership_reference` in the screening column and do not code it.

## 4. Identification fields (copied from the registers, not coded)

`record_id`, `corpus` (government / club / african_press / international_press), `case` (RWA / DRC / BOTH), `publication_date`, `language`, `institution_or_outlet`, `event_key`.

## 5. Variables for all corpora

### 5.1 Centrality

`partnership_centrality`: the place of the partnership in the document.

| Code | Rule |
|---|---|
| central | The partnership is the main subject of the headline or the opening paragraph; **or** the document reports a visit, ceremony, event, or programme that the text ties to the partnership by naming the partner as sponsor, host, inviter, or organizer. |
| secondary | The partnership is discussed in at least one full paragraph but is neither the main subject nor the occasion of the event reported. |
| passing | The partnership appears in a sentence, a clause, a list, a caption, or a logo reference only, and is not the occasion of the event reported. |
| implicit | Government and club documents only. The partnership is not named, but the document uses a partner club, its players or former players, its staff, its stadium, or its supporters to present the country. |

The second route to `central` is new in v0.3. A club delegation's trip to the sponsoring country, or a legends' tour hosted by the tourism board, exists because of the partnership even when the sponsorship is named once. Test: does the text name the partner as sponsor, host, inviter, or organizer of what is reported? If yes, code `central`.

**What each centrality level is coded for**

| Variables | central | secondary | implicit | passing |
|---|---|---|---|---|
| Scale and Africa references (5.4) | yes | yes | yes | yes |
| `conflict_link`, `accountability_scrutiny`, `scrutiny_stance` (5.2, 5.6) | yes | yes | yes | yes |
| `political_contact`, `other_case_mentioned` (5.7, 5.8) | yes | yes | yes | yes |
| Voices (5.10) | yes | yes | yes | yes, for the passing reference only |
| Other themes, `primary_narrative`, `initiative_attributed_to`, outcome claims, corpus-specific variables | yes | yes | yes | no |

In v0.2 a passing document lost everything except centrality and scale. A single clause can record parliamentary criticism or a link to conflict, so those variables are now coded at every level.

### 5.2 Themes

Code each theme on three levels.

| Code | Rule |
|---|---|
| 0 | Absent. |
| 1 | Mentioned: the theme appears in a phrase, a clause, or as one item in a list. |
| 2 | Developed: at least one full sentence is given to the theme. |

The three levels replace the yes/no coding of v0.2, which gave no threshold for a theme named in a single phrase. For analysis, "present" means 1 or 2, and the two can be reported separately.

| Variable | The theme is... |
|---|---|
| `tourism_promotion` | the partnership as promoting the country as a place to visit. |
| `investment_development` | investment, business, jobs, or economic development. |
| `sport_youth_development` | academies, coaching, training, or sport capacity in the country. |
| `cultural_identity` | national culture, heritage, creative work, or national products such as coffee and tea. |
| `international_visibility` | global reach, audience size, reputation, image, or recognition. |
| `conflict_link` | armed conflict or regional security, including eastern DR Congo and M23, connected to the partnership or to the state that sponsors it. A reference to "peace" with no reference to conflict is coded 0. |
| `accountability_scrutiny` | human rights, public spending, contract terms, payment, legality, harm to local football, fan or supporter objections, or oversight of the partnership. Code it whenever such criticism is present in the text, including when the text reports the criticism in order to reject it. The text's position is coded separately in `scrutiny_stance` (5.6). |

A text that anticipates criticism without naming any ("this is more than a logo") is coded 0 on `accountability_scrutiny`. Note it in `coder_note`.

### 5.3 Primary narrative

`primary_narrative`: the one account of the partnership that the document gives most space to. Choose one.

`tourism` / `investment_development` / `sport_capacity` / `culture_identity` / `visibility_recognition` / `political_defense` / `accountability_criticism` / `correction_of_record` / `mixed` / `other`

- `political_defense`: the document's main work is to answer criticism or justify the partnership.
- `accountability_criticism`: the main work is to question or criticize it.
- `correction_of_record` (new): the main work is to correct or clarify what others have reported about the partnership, without answering criticism of it.
- `mixed`: two accounts receive about equal space. Name both in `evidence_note`.

### 5.4 Scale and references to Africa

Two things were confused in v0.2: the unit a text treats as acting or benefiting, and the ways the word "Africa" can appear without making the continent that unit. They are now coded separately.

**`scale_of_reference`**: the unit the text uses when it says who acts, who benefits, or what the partnership means. Code the dominant scale.

| Code | Rule |
|---|---|
| national | Rwanda or DR Congo specifically: the country, its government, its people, its places. |
| regional | The Great Lakes region, East Africa, or Central Africa as the unit that acts or benefits. |
| continental | "Africa" or "Africans" as the unit that acts or benefits. |
| mixed | Two scales carry about equal weight. Name both in `evidence_note`. |

**Africa references**: code each 0 or 1. They record how the continent appears and do not by themselves change `scale_of_reference`.

| Variable | Code 1 when... | Example |
|---|---|---|
| `africa_in_slogan` | the continent appears in an official slogan, brand, or campaign name. | "Cœur d'Afrique" |
| `africa_as_comparison` | the continent is a ranking or comparison set. | "second fastest growing economy in Africa" |
| `africa_as_label` | the country is referred to by a continental or regional label in place of, or alongside, its name. | "the African country," "this Central African nation," "el país africano" |
| `africa_as_first_claim` | the text claims a first or only status defined by the continent. | "first African partner," "first sponsor from the African continent" |
| `africa_as_actor_or_beneficiary` | action, benefit, or meaning is attributed to Africa or Africans as a whole, or Africa is presented as the wider market or audience. | "inspiring millions across Africa" |

Rules:

1. `scale_of_reference` can be `continental` or `mixed` only if `africa_as_actor_or_beneficiary` is 1.
2. A slogan, a ranking, a label, or a first-claim never makes the scale continental. Code the marker and keep the scale the text otherwise uses.
3. Record who uses the reference when it is not the document's own voice (for example a quoted club executive) in `evidence_note`.

### 5.5 Who acts

`initiative_attributed_to`: who the text presents as the initiator or driver of the partnership.

`african_state` / `club` / `joint` / `third_party` / `not_stated`

- Code by how the text describes the decision. "X and Y have signed" or "have jointly decided" is `joint`. A state described as choosing, investing, or pursuing a strategy is `african_state`. A club described as selecting or supporting the country is `club`.
- When a joint signing and a one-sided framing both appear, code the framing the text gives more sentences to, and note the other.

### 5.6 Position on scrutiny

`scrutiny_stance`: what the text does with the criticism coded in `accountability_scrutiny` or the conflict coded in `conflict_link`.

| Code | Rule |
|---|---|
| raises | The criticism is the text's own line, or the line of the sources it gives most space. |
| reports | The criticism is attributed to others and is neither endorsed nor rejected. |
| rebuts | The criticism is reported in order to reject, answer, or correct it. Use this when the issuing institution answers criticism recorded in its own document. |
| not_applicable | `accountability_scrutiny` and `conflict_link` are both 0. |

This settles the v0.2 gap: criticism that a text rebuts is still criticism present in the text. Rwanda's reply to DR Congo is coded `accountability_scrutiny` 2 and `scrutiny_stance` rebuts.

### 5.7 Political contact

`political_contact` (new): whether the text reports a meeting, signing, hosting, or joint appearance between representatives of a club (executives, staff, current or former players) and officials of Rwanda or DR Congo.

| Code | Rule |
|---|---|
| head_of_state_or_government | A president or prime minister. |
| minister | A minister or deputy minister, with no head of state or government. |
| senior_official | The head of a state agency or tourism board (for example the chief executive of the Rwanda Development Board), an ambassador or high commissioner, or another senior state official, with no minister or head of state. |
| none | No such contact is reported. |

Rules:

1. Code the highest level reported.
2. The contact must be reported as an event: the people met, signed, appeared together, or one hosted the other. A press release that quotes a club executive and a state official side by side, without saying they met or signed together, is `none`.
3. Both sides must be present. A state official hosting guests at a club's stadium with no club representative reported is `none`.
4. Heads of football federations are not state officials for this variable. Code them under `voice_football_body` if they are quoted.

### 5.8 Other state mentioned

`other_case_mentioned` (0/1): a text about Rwanda's partnership mentions DR Congo, or a text about DR Congo's partnership mentions Rwanda.

### 5.9 Claims of outcome

- `claimed_outcome` (0/1): the text asserts that the partnership has produced a result (visitors, revenue, reach, awards, players trained). A figure that predates the partnership, or an aim stated in the future tense, is 0.
- `outcome_claimed_by`: `government` / `club` / `journalist` / `other_source` / `not_applicable`.
- `independent_evidence_in_document`: `yes` / `no` / `unclear` / `not_applicable`. Code `yes` only when the text gives separately sourced evidence with a stated method. Code `unclear` when figures or research are cited without a source or method.

Use `not_applicable` for both when `claimed_outcome` is 0. Log each specific figure in the claim register. Do not treat a claimed figure as established.

### 5.10 Voices

Code 1 for each type of source that is quoted, or paraphrased with attribution.

`voice_government_rwa`, `voice_government_drc`, `voice_club`, `voice_football_body`, `voice_fans_supporters`, `voice_civil_society`, `voice_international_body` (United Nations and similar), `voice_expert_academic`, `voice_opposition_or_parliament`, `voice_business` (new: investors, company founders, sponsors other than the club), `voice_citizens`, `voice_other_media`.

Rules:

1. The institution that issues a document is its author, not a voice. Code a government or club voice only when a named person or body is quoted or paraphrased with attribution. An unsigned government statement has no `voice_government` code for itself.
2. A position attributed to another party counts even when it is paraphrased in order to be rejected.
3. For `passing` documents, code voices for the passing reference only.

## 6. Additional variables: government and club documents

`document_function`: what the document does. Choose one.

`announcement` / `renewal_or_extension` / `activation_or_visit` / `programme_report` / `response_to_criticism` / `correction_of_reports` / `change_or_exit` / `official_minutes` / `standing_page` / `other`

- `correction_of_reports` (new): the document corrects or clarifies media or public accounts of the partnership.
- `response_to_criticism`: the document answers criticism of the partnership itself.

Not coded for `passing` documents.

**Club response to criticism** (club documents only). In v0.2 this was one variable with one value, but a club can do several of these at once. Code each 0 or 1, and code all three `not_applicable` when `accountability_scrutiny` is 0.

| Variable | Code 1 when the club... |
|---|---|
| `club_defends_partnership` | justifies the partnership by its benefits, its vetting, or its results. |
| `club_separates_from_politics` | says the club has no part in, or no view on, the state's policies or politics. |
| `club_announces_change` | announces a change to the partnership in the same document. |

## 7. Additional variables: news items

| Variable | Codes | Rule |
|---|---|---|
| `origin` | own_reporting / wire / republished / opinion / unclear | Byline and credit line decide. A staff byline with wire material credited is own_reporting. |
| `genre` | news / analysis / feature / opinion / sports_brief | Use the outlet's own label where there is one. |
| `narrative_uptake` | relays / qualifies / contests / not_addressed | How the item treats the sponsoring state's own account. See the rules below. |
| `stance` | favorable / neutral / mixed / critical | The item's overall evaluation of the partnership. Code neutral when the item reports without evaluating. |
| `sportswashing_term` | not_used / used_attributed / used_in_own_voice | Whether "sportswashing" or a direct equivalent appears, and whose words it is. |

Rules for `narrative_uptake`:

- **relays:** the item reports the state's or club's stated aims or claims without challenge or counter-source.
- **qualifies:** the item reports them and adds context, a limit, or another source that complicates them, without rejecting them.
- **contests:** the item's main line rejects or disputes them, in its own voice or through sources it gives the most space.
- **not_addressed:** the item covers the partnership without reporting the state's or club's account of it.

`narrative_uptake` and `stance` are separate. An item can relay a government claim and remain neutral, or contest it while quoting it at length.

These press variables were not tested in the pilot, which used government and club documents only. They need their own pilot once the press items are verified.

## 8. General coding rules

1. Read the whole document, or the whole relevant passage, before coding. Do not code from the title, the register note, the verification file, or a summary produced by software.
2. Code what is stated. Do not infer intent.
3. Code French, German, Spanish, and Italian texts in the original language. A machine translation may be used as an aid, never as the text coded. Browsers may translate pages without asking: check that the page is in its original language before reading.
4. Record in `text_basis` how the text was read: in full in the original, in translation, or from an extract. A code made from a translation or an extract is provisional until the original is read.
5. For every document, fill `evidence_note` with the location of the passages that decided the main codes (paragraph number or section) and a paraphrase of no more than one sentence each. Do not paste article text into the sheet.
6. When a rule does not settle a case, choose the closest code, describe the problem in `coder_note`, and add it to the decision log. Do not invent a new code while coding.
7. Images and video are not coded in this version.

## 9. Procedure

1. **Pilot.** Done on 2026-11-19 with ten government and club documents and v0.2.
2. **Revise.** Done: this version. The pilot documents were recoded with it.
3. **Second pilot for the press.** Code about ten news items once the press registers are verified, and revise section 7 if needed.
4. **Full coding.** Code all eligible documents.
5. **Consistency check.** After full coding, recode a random 15 percent of documents without looking at the first codes, and report agreement between the two passes for each variable. This is a check of one coder's consistency over time. It is not intercoder reliability and must not be reported as such.
6. **Record of assistance.** If software or an AI system proposes codes, the sheet keeps the proposal and the researcher's final decision in separate columns, and the methods section says so.

## 10. What each variable is for

| Question | Variables |
|---|---|
| What account does each state and club give of the partnership? | themes, `primary_narrative`, `document_function`, `claimed_outcome` |
| Do the two states, the clubs, and the press speak of nations or of "Africa," and in what way? | `scale_of_reference`, the five Africa references, `initiative_attributed_to` |
| How does each press stratum treat those accounts? | `narrative_uptake`, `stance`, `sportswashing_term`, voices |
| When does conflict or accountability enter, through whom, and how is it met? | `conflict_link`, `accountability_scrutiny`, `scrutiny_stance`, voices, `other_case_mentioned` |
| How do clubs respond when the partnership is questioned or misreported? | the three club response variables, `document_function`, `correction_of_record` |
| Does the partnership bring clubs into contact with political leaders? | `political_contact` |

## 11. Variables at a glance

| Group | Variables | Values |
|---|---|---|
| Centrality | `partnership_centrality` | central / secondary / passing / implicit |
| Themes | seven theme variables | 0 / 1 / 2 |
| Narrative | `primary_narrative` | ten values |
| Scale | `scale_of_reference` | national / regional / continental / mixed |
| Africa references | five variables | 0 / 1 |
| Agency | `initiative_attributed_to` | five values |
| Scrutiny | `scrutiny_stance` | raises / reports / rebuts / not_applicable |
| Politics | `political_contact` | head_of_state_or_government / minister / senior_official / none |
| Other case | `other_case_mentioned` | 0 / 1 |
| Outcomes | `claimed_outcome`, `outcome_claimed_by`, `independent_evidence_in_document` | see 5.9 |
| Voices | twelve voice variables | 0 / 1 |
| Government and club | `document_function`, three club response variables | see 6 |
| Press | `origin`, `genre`, `narrative_uptake`, `stance`, `sportswashing_term` | see 7 |

## 12. Changes from v0.2, and the pilot case behind each

| Problem found in the pilot | Change | Pilot case |
|---|---|---|
| The passing rule discarded important content. | Passing documents are now coded for conflict, scrutiny, scrutiny stance, political contact, the other case, and voices (5.1). | GOV-DRC-006: one clause records a Senate commission judging the deals harmful to local clubs. |
| Visits and events were miscoded on centrality. | A visit, ceremony, event, or programme tied to the partner by the text is `central` (5.1). | CLUB-010: a club delegation's trip to Rwanda, with the sponsorship named once. |
| Nothing recorded political contact. | New variable `political_contact` (5.7). | CLUB-010: the club's chief executive meets the president. |
| No code for correcting the press. | New `correction_of_record` under primary narrative and `correction_of_reports` under document function (5.3, 6). | CLUB-006: a statement correcting reports that the partnership had ended. |
| Scale had no rules for slogans, rankings, or continental labels. | Scale is separated from five Africa-reference variables, with rules for each (5.4). "First African partner" is now a first-claim, not evidence of continental scale. | GOV-DRC-001 (slogan), GOV-RWA-001 (ranking), CLUB-018 and CLUB-010 (label). |
| Rebutted criticism was undefined. | Criticism is coded as present even when rebutted; new variable `scrutiny_stance` records the text's position (5.2, 5.6). | GOV-RWA-012: Rwanda's reply to DR Congo. |
| No voice code for business people. | New `voice_business` (5.10). | GOV-RWA-011: fintech founders quoted. |
| No value when no outcome is claimed. | `not_applicable` added to the two outcome follow-ups (5.9). | Seven of the ten pilot documents. |
| The club criticism variable allowed one value. | Replaced by three yes/no variables (6). | CLUB-002: the club both defends the partnership and separates itself from politics. |
| No threshold for a theme named in one phrase. | Themes are coded 0, 1 (mentioned), or 2 (developed) (5.2). | GOV-RWA-011: culture and tourism in one closing phrase. |
| The issuing institution's own voice was ambiguous. | The issuer is the author, not a voice (5.10). | GOV-RWA-012: an unsigned government statement. |
| Passages in long documents had no centrality rule. | Centrality is judged within the passage (2). | GOV-DRC-008, CLUB-002. |
| A browser translated French pages without notice. | Rule 3 and the new `text_basis` field (8). | GOV-DRC-001, GOV-DRC-006. |
