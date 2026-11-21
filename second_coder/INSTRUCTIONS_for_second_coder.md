# Instructions for the second coder

You are coding documents for a content analysis of European football club partnerships with Rwanda and with DR Congo. Another coder has already coded these documents. You must not see that coding. Work only from the files in this packet and from the source pages.

## What you have

- `codebook_v0.4_for_second_coder.md`: the rules. Read all of it before coding anything.
- `blank_coding_sheet.csv`: one row per document, with identification filled in and every coding column empty.
- `texts/`: the full text of some documents, named by record ID. Use these where present. For the rest, read the page at `source_url`.

## What you must not use

- The project's public repository, its data folder, its decision log, or any earlier coding file.
- Any summary, report or discussion of the results.
- Other documents in the corpus when coding a given document. Code each one from its own text.

## How to code

1. Code from the original language. If you can only read a translation, say so in `text_basis`.
2. Fill every coding column the codebook requires for that document's centrality level. Leave columns blank only where the codebook says they are not coded.
3. In `evidence_note`, give the paragraph or passage behind every code that is not 0, in your own words or a short quotation.
4. Where you are unsure, choose the code the rules best support and explain the doubt in `coder_note`. Do not guess silently, and do not skip the document.
5. Do not add codes that are not in the codebook. If none fits, use the closest and say so in `coder_note`.
6. If a page will not load or is behind a wall, record that in `text_basis` and code only what you could read, using `not_established` for the rest.
7. Rows marked PARTIAL in `read_status` can only ever be read in part. Apply rule 6.

## Which documents

The column `in_25_percent_sample` marks a random quarter of each group, drawn in advance with a fixed seed. The researcher will tell you whether to code the sample or every row.

## What to return

The completed `blank_coding_sheet.csv`, with your name or model in `coder` and the date in `coded_on`. Change nothing in the identification columns.
