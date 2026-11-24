# Data Dictionary

`transactions_raw.csv`: transaction_id, transaction_date, customer_id, product_id, quantity, unit_price, sales_amount, region, category, channel, status. Intentional defects are present.

`customers.csv`: customer_id, customer_name, region, segment.

`products.csv`: product_id, product_name, category, standard_price.

`transactions_clean.csv`: standardized transaction rows that pass every configured validation rule.

`data_quality_issues.csv`: one record per violation with transaction_id, rule_code, dimension, severity and issue_description. A transaction may appear multiple times.
