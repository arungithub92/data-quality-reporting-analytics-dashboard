USE data_quality_analytics;
-- Duplicate IDs
SELECT transaction_id,COUNT(*) occurrences FROM transactions_raw GROUP BY transaction_id HAVING COUNT(*)>1;
-- Missing mandatory values
SELECT SUM(customer_id IS NULL OR TRIM(customer_id)='') missing_customer,SUM(product_id IS NULL OR TRIM(product_id)='') missing_product,SUM(sales_amount IS NULL) missing_sales,SUM(region IS NULL OR TRIM(region)='') missing_region FROM transactions_raw;
-- Invalid customer/product keys
SELECT t.* FROM transactions_raw t LEFT JOIN customers c ON c.customer_id=t.customer_id LEFT JOIN products p ON p.product_id=t.product_id WHERE c.customer_id IS NULL OR p.product_id IS NULL;
-- Invalid quantities and prices
SELECT * FROM transactions_raw WHERE quantity<=0 OR unit_price<=0;
-- Sales reconciliation
SELECT *,ROUND(quantity*unit_price,2) calculated_sales,ROUND(sales_amount-quantity*unit_price,2) variance FROM transactions_raw WHERE sales_amount IS NOT NULL AND ABS(sales_amount-quantity*unit_price)>.01;
-- Inspect inconsistent labels
SELECT DISTINCT region FROM transactions_raw ORDER BY region;
SELECT DISTINCT category FROM transactions_raw ORDER BY category;
-- Raw count and duplicate excess
SELECT COUNT(*) raw_rows,COUNT(DISTINCT transaction_id) distinct_ids,COUNT(*)-COUNT(DISTINCT transaction_id) duplicate_excess FROM transactions_raw;
