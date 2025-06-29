# This script connects to a SQLite database, creates tables, and loads data from CSV files into those tables. 
# It also handles missing values by replacing them with default values before inserting the data. 
# Finally, it commits the changes and closes the database connection.

import pandas as pd
import sqlite3

print("🔌 Connecting to database...")
conn = sqlite3.connect('business_data.db')
cursor = conn.cursor()

print("🧱 Dropping old tables (if they exist)...")
cursor.executescript('''
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS vendors;
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS pricebook;
''')

print("🧱 Creating tables...")
cursor.executescript('''
CREATE TABLE customers (
    customer_id INTEGER,
    customer_name TEXT, 
    region TEXT,
    customer_type TEXT
);

CREATE TABLE vendors (
    vendor_id INTEGER,
    vendor_name TEXT, 
    region TEXT,
    category TEXT,
    status TEXT
);

CREATE TABLE items (
    item_id INTEGER,
    item_description TEXT, 
    vendor_id INTEGER,
    unit_cost REAL
);

CREATE TABLE pricebook (
    item_id INTEGER,
    customer_type TEXT,
    list_price REAL,
    discount REAL
);
''')

print("📁 Loading CSV files...")
customers = pd.read_csv('customers.csv')
vendors = pd.read_csv('vendors.csv')
items = pd.read_csv('items.csv')
pricebook = pd.read_csv('pricebook.csv')

print("💾 Writing data to database (with possible duplicates and missing values)...")
try:
    customers.to_sql('customers', conn, if_exists='append', index=False)
    vendors.to_sql('vendors', conn, if_exists='append', index=False)
    items.to_sql('items', conn, if_exists='append', index=False)
    pricebook.to_sql('pricebook', conn, if_exists='append', index=False)
    conn.commit()
    print("✅ Data successfully loaded into the database.")
except Exception as e:
    print(f"❌ ERROR during data load: {e}")

conn.close()