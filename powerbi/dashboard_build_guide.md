# Power BI Dashboard Build Guide

## Model
Load raw transactions, clean transactions, issue log, customers and products. Relate customers and products to clean transactions using their keys. Use a distinct transaction dimension if needed to connect clean records and issue records without ambiguous filter paths. Add a Date table for clean transaction date.

## Page 1 — Executive Overview
Cards: Raw Rows, Distinct IDs, Duplicate Row Excess, Clean Rows, Rows With Issues, Quality Score %. Charts: issue records by dimension/rule; clean vs affected transactions; quality score summary.

## Page 2 — Quality Dimensions
Visuals for completeness, uniqueness, validity, referential integrity, consistency and accuracy. Include missing fields, invalid keys, negative numeric values and sales reconciliation exceptions.

## Page 3 — Issue Monitoring
Issue detail table with transaction ID, rule, dimension, severity and description; severity and rule slicers; drill-through to transaction details; raw-vs-clean reconciliation.

## Interpretation
A transaction may create multiple issue records. Rows With Issues is a distinct transaction count; Issue Records is a rule-violation count. Quality Score = clean rows / raw source rows. Duplicate excess rows remain in the denominator. State this project-specific definition.
