# Power Query Guide

Run `python src/profile_and_clean.py` first. Import `data/cleaned/transactions_clean.csv`, `data/cleaned/data_quality_issues.csv`, `data/raw/transactions_raw.csv`, and both reference CSVs.

For clean transactions, set transaction_date to Date, quantity to Whole Number, unit_price and sales_amount to Decimal/Currency, and identifiers/labels to Text. Trim text fields. For the issue log, set IDs, rule_code, dimension, severity and description to Text.

The Python pipeline owns auditable cleansing. Power Query handles import, data types and report-layer shaping. Keep raw source unchanged.
