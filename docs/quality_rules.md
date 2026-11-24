# Quality Rules

| Rule | Dimension | Condition | Handling |
|---|---|---|---|
| DUPLICATE_TRANSACTION_ID | Uniqueness | ID occurs more than once | Keep first; log later copies |
| MISSING_CUSTOMER_ID | Completeness | Customer key blank | Quarantine |
| MISSING_SALES_AMOUNT | Completeness | Sales blank | Quarantine |
| MISSING_REGION | Completeness | Region blank | Quarantine |
| INVALID_TRANSACTION_DATE | Validity | Date not ISO or DD/MM/YYYY | Quarantine |
| INVALID_QUANTITY | Validity | Quantity <= 0 or noninteger | Quarantine |
| INVALID_UNIT_PRICE | Validity | Price <= 0 or nonnumeric | Quarantine |
| INVALID_CUSTOMER_KEY | Referential integrity | Customer not in reference | Quarantine |
| INVALID_PRODUCT_KEY | Referential integrity | Product not in reference | Quarantine |
| NONSTANDARD_REGION | Consistency | Region differs from customer reference | Flag; canonicalize only if row otherwise valid |
| NONSTANDARD_CATEGORY | Consistency | Category differs from product reference | Flag; canonicalize only if row otherwise valid |
| SALES_AMOUNT_MISMATCH | Accuracy | Sales != quantity × price (tolerance 0.01) | Quarantine |

Issue counts by rule overlap. The clean output contains only rows with zero violations.
