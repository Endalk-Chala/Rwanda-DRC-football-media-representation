# Codebook v0.2 (draft for pilot)

**Status:** draft, 2026-11-19. Not yet piloted. Nothing has been coded with it.
**Replaces:** [codebook_v0.1.md](codebook_v0.1.md), which covered government documents only.
**Covers:** all three corpora: government communications, European club communications, and journalism (African and international press).

## 1. Purpose

The codebook supports one comparative question: how do Rwanda and DR Congo present their partnerships with European football clubs, how do the clubs present them, and how do news organizations in Africa, Europe, and the United States relay, qualify, or contest those presentations?

The variables record what a text says. They do not record whether a campaign worked, and no variable should be read as a measure of effect.

## 2. Unit of analysis

One unit is one distinct document: a government web page or official minute, a club page or document, or a news item.

- A translation or language version of a document already in the corpus is linked to its master record and coded once (example: GOV-RWA-030 is coded under GOV-RWA-007).
- A wire story republished by another outlet is coded once, under the wire master record. The republication is logged, not coded again.
- For long documents that address the partnership in one part only (council minutes, a fans' forum record, a season review), code only the passage about the partnership and record its location in `evidence_note`.

## 3. Eligibility

Code a document only if it meets both conditions:

1. It was published between 2018-01-01 and 2026-11-13.
2. It refers to a partnership, sponsorship, or cooperation between Rwanda or DR Congo (the state, a state agency, or the national tourism brand) and a European football club.

A document that names a club without referring to the partnership is not eligible. Record it as `excluded_no_partnership_reference` in the screening column and do not code it.

## 4. Identification fields (copied from the registers, not coded)

`record_id`, `corpus` (government / club / african_press / international_press), `case` (RWA / DRC / BOTH), `publication_date`, `language`, `institution_or_outlet`, `event_key`.

## 5. Variables for all corpora

### 5.1 Centrality

`partnership_centrality`: how much of the document is about the partnership.

| Code | Rule |
|---|---|
| central | The partnership is the main subject of the headline or the opening paragraph. |
| secondary | The partnership is discussed in at least one full paragraph but is not the main subject. |
| passing | The partnership appears in a sentence, a list, a caption, or a logo reference only. |

Documents coded `passing` receive the identification fields, centrality, and `scale_of_reference` only. The remaining variables are left blank.

### 5.2 Themes present

Code each theme 1 if the text states it explicitly, 0 if it does not, and `unclear` if you cannot decide after rereading. Several themes may be present.

| Variable | Code 1 when the text... |
|---|---|
| `tourism_promotion` | presents the partnership as promoting the country as a place to visit. |
| `investment_development` | links the partnership to investment, business, jobs, or economic development. |
| `sport_youth_development` | describes academies, coaching, training, or sport capacity in the country. |
| `cultural_identity` | invokes national culture, heritage, creative work, or national products such as coffee and tea. |
| `international_visibility` | refers to global reach, audience size, reputation, image, or recognition. |
| `conflict_link` | connects the partnership to armed conflict or regional security, including eastern DR Congo and M23. |
| `accountability_scrutiny` | raises human rights, public spending, contract terms, payment, legality, fan or supporter objections, or oversight of the partnership. |

`conflict_link` and `accountability_scrutiny` replace the single `conflict_accountability` variable in v0.1, because a text can raise one without the other.

### 5.3 Primary narrative

`primary_narrative`: the one account of the partnership that the document gives most space to. Choose one.

`tourism` / `investment_development` / `sport_capacity` / `culture_identity` / `visibility_recognition` / `political_defense` / `accountability_criticism` / `mixed` / `other`

- Use `political_defense` when the document's main work is to answer criticism or justify the partnership.
- Use `accountability_criticism` when the main work is to question or criticize it.
- Use `mixed` only when two accounts receive about equal space. Name both in `evidence_note`.

### 5.4 Scale of reference

`scale_of_reference`: the geographic or political unit the text uses when it says who acts, who benefits, or what the partnership means.

| Code | Rule |
|---|---|
| national | The text speaks of Rwanda or DR Congo specifically (the country, its government, its people, its places). |
| regional | The text frames the matter through the Great Lakes region, East Africa, or Central Africa. |
| continental | The text attributes action, benefit, or meaning to "Africa" or "African" as a whole (for example "first African partner," "a continent of opportunities"). |
| mixed | Two scales are used with about equal weight. Name both in `evidence_note`. |

Code what the text does, not what the coder knows about the country.

### 5.5 Who acts

`initiative_attributed_to`: who the text presents as the initiator or driver of the partnership.

`african_state` / `club` / `joint` / `third_party` / `not_stated`

### 5.6 Other state mentioned

`other_case_mentioned` (0/1): a text about Rwanda's partnership mentions DR Congo, or a text about DR Congo's partnership mentions Rwanda.

### 5.7 Claims of outcome

- `claimed_outcome` (0/1): the text asserts that the partnership has produced a result (visitors, revenue, reach, awards, players trained).
- `outcome_claimed_by`: `government` / `club` / `journalist` / `other_source` / blank.
- `independent_evidence_in_document` (yes / no / unclear): the text gives separately sourced evidence with a stated method, not only a figure reported by the party that benefits.

Log each specific figure in the claim register. Do not treat a claimed figure as established.

### 5.8 Voices

Code 1 for each type of source that is quoted or paraphrased with attribution.

`voice_government_rwa`, `voice_government_drc`, `voice_club`, `voice_football_body`, `voice_fans_supporters`, `voice_civil_society`, `voice_international_body` (United Nations and similar), `voice_expert_academic`, `voice_opposition_or_parliament`, `voice_citizens`, `voice_other_media`.

## 6. Additional variables: government and club documents

`document_function`: what the document does. Choose one.

`announcement` / `renewal_or_extension` / `activation_or_visit` / `programme_report` / `response_to_criticism` / `change_or_exit` / `official_minutes` / `standing_page` / `other`

`criticism_addressed` (club documents only): how the club deals with criticism of the partnership.

`not_addressed` / `defends_partnership` / `separates_club_from_politics` / `announces_change`

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

## 8. General coding rules

1. Read the whole document, or the whole relevant passage, before coding. Do not code from the title, the register note, or the verification file.
2. Code what is stated. Do not infer intent.
3. Code French, German, Spanish, and Italian texts in the original language. A machine translation may be used as an aid, never as the text coded.
4. For every document, fill `evidence_note` with the location of the passages that decided the main codes (paragraph number or section) and a paraphrase of no more than one sentence. Do not paste article text into the sheet.
5. When a rule does not settle a case, choose `unclear`, describe the problem in `coder_note`, and add it to the decision log. Do not invent a new code while coding.
6. Images and video are not coded in this version.

## 9. Procedure

1. **Pilot.** Code 10 documents that vary by case, corpus, and language. Record every difficulty.
2. **Revise.** Change the rules, issue the codebook as v0.3, and recode the pilot documents.
3. **Full coding.** Code all eligible documents.
4. **Consistency check.** After full coding, recode a random 15 percent of documents without looking at the first codes, and report agreement between the two passes for each variable. This is a check of one coder's consistency over time. It is not intercoder reliability and must not be reported as such.
5. **Record of assistance.** If software or an AI system proposes codes, the sheet keeps the proposal and the researcher's final decision in separate columns, and the methods section says so.

## 10. What each variable is for

| Question | Variables |
|---|---|
| What account does each state and club give of the partnership? | themes, `primary_narrative`, `document_function`, `claimed_outcome` |
| Do the two states present themselves as nations or as part of "Africa," and does the press follow them? | `scale_of_reference`, `initiative_attributed_to` |
| How does each press stratum treat those accounts? | `narrative_uptake`, `stance`, `sportswashing_term`, voices |
| When does conflict or accountability enter the coverage, and through whom? | `conflict_link`, `accountability_scrutiny`, voices, `other_case_mentioned` |
| How do clubs respond when the partnership is questioned? | `criticism_addressed`, `document_function` |

## 11. Changes from v0.1

- Extended from government documents to all three corpora.
- Added eligibility and centrality rules, so passing mentions are not coded as if they were statements about the partnership.
- Split `conflict_accountability` into `conflict_link` and `accountability_scrutiny`.
- Added `scale_of_reference`, `initiative_attributed_to`, `other_case_mentioned`, the voice variables, and the press variables.
- Added decision rules for each variable and a single-coder consistency check.
