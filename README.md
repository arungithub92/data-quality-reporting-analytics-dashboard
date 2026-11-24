# Data Quality & Reporting Analytics Dashboard

Portfolio project demonstrating data profiling, validation, cleansing, reconciliation and monitoring using Python, SQL, Power BI, DAX and Power Query. All data is synthetic; intentional defects are included for learning and do not represent any real company.

## Business questions
- How many records are received, duplicated, affected, clean or quarantined?
- Which fields have the highest missing-value rates?
- How many records have invalid customer/product keys, quantities, prices or dates?
- Which sales amounts fail quantity × unit-price reconciliation?
- How does data quality vary by rule, dimension, region and category?

## Repository
- `data/raw/`: immutable source transactions
- `data/reference/`: customer and product lookup tables
- `data/cleaned/`: curated clean transactions and row-level issue log
- `sql/`: MySQL schema and validation queries
- `powerbi/`: DAX, Power Query and dashboard guide
- `src/`: reproducible dataset generator and profiler/cleaner
- `docs/`: data dictionary, rules and generated quality summary
- `reports/`: rule-level profiling summary

## Dataset
5,000 source transaction IDs plus 75 duplicated rows; 500 customers; 40 products; transaction dates in 2025. Defects include nulls, duplicate IDs, invalid foreign keys, negative quantities/prices, inconsistent labels, mixed date formats and sales arithmetic mismatches.

## Run
```bash
python -m pip install -r requirements.txt
python src/profile_and_clean.py
```
The script writes clean transactions, one-row-per-rule issue records, profiling CSV and JSON summary. Raw input is never overwritten.

## Power BI pages
1. Executive overview: raw rows, distinct IDs, duplicate excess, clean rows, affected rows, quality score and issue distribution.
2. Quality dimensions: completeness, uniqueness, validity, referential integrity, consistency and accuracy.
3. Issue monitoring: issue log, severity, rule counts, affected transaction drill-through and raw-vs-clean reconciliation.

## Quality logic
A transaction is clean only if it passes every configured rule. Duplicate handling retains the first transaction ID occurrence. A row can have multiple issue records, so issue records may exceed unique affected transactions. Quality score = clean rows / raw source rows. This is a project-defined record-level metric; always state its denominator. Duplicate excess rows remain in the raw-row denominator.

## Interview talking points
Explain profiling vs cleansing vs monitoring, duplicate handling, foreign-key checks, source-to-target reconciliation, immutable raw data, overlapping issue counts and quality-score design.

## Limitations
Synthetic single-year data and deterministic remediation rules. In production, agree rules with data owners, log lineage and approvals, preserve historical snapshots, and add alerting and quality SLAs.
