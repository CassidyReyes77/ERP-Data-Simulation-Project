# Data Dictionary

This data dictionary describes the tables and fields used in the ERP Data Simulation Project.

---

## 📋 customers.csv

| Column Name     | Data Type | Description                      |
|-----------------|-----------|----------------------------------|
| customer_id     | Integer   | Unique customer ID (Primary Key) |
| customer_name   | String    | Name of the customer             |
| region          | String    | US state or region               |
| customer_type   | String    | 'Retail' or 'Wholesale'          |

---

## 📋 vendors.csv

| Column Name     | Data Type | Description                      |
|-----------------|-----------|----------------------------------|
| vendor_id       | Integer   | Unique vendor ID (Primary Key)   |
| vendor_name     | String    | Name of the vendor               |
| region          | String    | Vendor's region                  |
| category        | String    | Product category (e.g., Electronics, Food) |
| status          | String    | 'Active' or 'Inactive'           |

---

## 📋 items.csv

| Column Name     | Data Type | Description                      |
|-----------------|-----------|----------------------------------|
| item_id         | Integer   | Unique item ID (Primary Key)     |
| item_description| String    | Product description              |
| vendor_id       | Integer   | Foreign key to `vendors.vendor_id` |
| unit_cost       | Float     | Cost of one unit (USD)           |

---

## 📋 pricebook.csv

| Column Name     | Data Type | Description                      |
|-----------------|-----------|----------------------------------|
| item_id         | Integer   | Foreign key to `items.item_id`   |
| customer_type   | String    | 'Retail' or 'Wholesale'          |
| list_price      | Float     | Listed selling price (USD)       |
| discount        | Float     | Discount as a decimal (e.g., 0.15 = 15%) |

---

## 📋 audit_log (SQLite Table)

| Column Name     | Data Type | Description                           |
|-----------------|-----------|---------------------------------------|
| id              | Integer   | Auto-incrementing ID                  |
| table_name      | String    | Name of the affected table            |
| issue_type      | String    | Type of issue (e.g., Duplicate, Null) |
| details         | String    | Description of the issue              |
| timestamp       | Datetime  | When the issue was logged             |
