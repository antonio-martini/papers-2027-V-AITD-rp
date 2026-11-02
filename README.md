# Anonymous replication package

This package traces 63 anonymous statement IDs to nine predefined content codes, 22 questionnaire items, and the paper's correlations and descriptive patterns. Six CSV inputs underpin the traceability report, reproduction script, and validation record.

Start with [TRACEABILITY.md](TRACEABILITY.md). It contains the codebook, questionnaire wording, all reported correlations, reverse indexes of linked statements, and each statement's question context and connections. Every anonymous statement ID appears once in the statement traceability section.

## Data files

| File | Purpose |
| --- | --- |
| [statement_anonym.csv](data/statement_anonym.csv) | The 63 anonymous statement IDs and their question context (`statement_id`, `direction`) |
| [codebook.csv](data/codebook.csv) | The nine coding definitions and their recorded increase/decrease counts |
| [questionnaire_items.csv](data/questionnaire_items.csv) | The 22 selected items, question wording, internal and manuscript IDs, and recorded coverage counts |
| [correlations.csv](data/correlations.csv) | Only the paper's 66 numerical correlations, plus mapping metadata and archived aliases for the 14 correlations included in the qualitative mapping |
| [patterns.csv](data/patterns.csv) | The ten descriptive figure patterns, stable manuscript references, and archived aliases |
| [links.csv](data/links.csv) | All 466 connections: 224 statement–code assignments, 96 questionnaire-item connections, and 146 correlation/pattern connections |

Statement IDs join `links.csv` to `statement_anonym.csv`. The `target_type` field determines which catalog contains `target_id`: `theme` uses `codebook.csv`, `questionnaire_item` uses `questionnaire_items.csv`, `correlation` uses `correlations.csv`, and `pattern` uses `patterns.csv`.

In this package, a **theme** is one of the nine predefined content categories in the paper's qualitative codebook, such as `process`, `benefit`, or `limitation`. It labels what a statement discusses. For example, `DEC-14,theme,process` records that statement DEC-14 describes a development or maintenance activity. A statement can have several theme links when it covers several categories.

Links contain three fields: `statement_id`, `target_type`, and `target_id`. Statements may have several codes and several connections. The type field distinguishes content-code assignments, questionnaire connections, correlations, and patterns.

Target metadata, aliases, and coverage counts are stored in the relevant catalog. Code assignments are recorded in `links.csv`.

## Reproduce and validate

Run from the package folder:

```sh
python3 scripts/reproduce.py
```

Or run from the enclosing project folder:

```sh
python3 papers-2027-V-AITD-rp/scripts/reproduce.py
```

Input and output paths are resolved relative to the script's package folder, independently of the working directory.

No external dependencies or private inputs are needed. The script regenerates [TRACEABILITY.md](TRACEABILITY.md) and [validation.json](validation.json). Validation checks the statement schema, paper scope, unique identifiers, resolved links, target types, numerical fields, archived aliases, and code/item counts. The validation record also contains file checksums. It excludes itself from checksum calculation.

## Coding and connections

The existing deductive analysis uses nine overlapping content categories: type of debt, tool, process, benefit, limitation, example, specification, scope, and decision. The documented analysis used automated mapping assistance with researcher-provided rules, followed by verification by one researcher. Coding predates the anonymous summaries. Sixty statements received at least one code; three entries lack assessable substantive content.

| Target type | Meaning |
| --- | --- |
| Theme | Links a statement to a predefined content category in `codebook.csv` |
| Questionnaire item | Links a statement to a selected survey topic |
| Correlation | Links a statement to a reported numerical association |
| Pattern | Links a statement to a descriptive figure relationship |

## Anonymization

Statement inputs contain only anonymous IDs and question context. Statement text, coding rationales, result readings, and evidential notes are not included. Statement IDs identify entries rather than respondents.

The original content-code assignments and mapping links are preserved.

Participant-level quantitative records and verified links between comments and questionnaire scores are excluded. The numerical correlations therefore cannot be independently recalculated from this package.
