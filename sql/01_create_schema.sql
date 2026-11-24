CREATE DATABASE IF NOT EXISTS data_quality_analytics;
USE data_quality_analytics;
CREATE TABLE customers(customer_id VARCHAR(10) PRIMARY KEY,customer_name VARCHAR(100),region VARCHAR(40),segment VARCHAR(40));
CREATE TABLE products(product_id VARCHAR(10) PRIMARY KEY,product_name VARCHAR(100),category VARCHAR(60),standard_price DECIMAL(12,2));
CREATE TABLE transactions_raw(transaction_id VARCHAR(20),transaction_date VARCHAR(20),customer_id VARCHAR(10),product_id VARCHAR(10),quantity INT,unit_price DECIMAL(12,2),sales_amount DECIMAL(14,2),region VARCHAR(40),category VARCHAR(60),channel VARCHAR(40),status VARCHAR(30));
CREATE INDEX idx_raw_id ON transactions_raw(transaction_id);
CREATE INDEX idx_raw_customer ON transactions_raw(customer_id);
CREATE INDEX idx_raw_product ON transactions_raw(product_id);
