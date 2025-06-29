import sqlite3
import pandas as pd

print("🔌 Connecting to database...")
conn = sqlite3.connect('business_data.db')
cursor = conn.cursor()

print("🧱 Creating audit log table...")
cursor.execute('''
CREATE TABLE IF NOT EXISTS audit_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_name TEXT,
    issue_type TEXT,
    details TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
''')

def log_issue(table_name, issue_type, details):
    cursor.execute('''
        INSERT INTO audit_log (table_name, issue_type, details)
        VALUES (?, ?, ?);
    ''', (table_name, issue_type, details))

# Duplicate check
print("🔍 Checking for duplicates...")
for table in ['customers', 'vendors', 'items', 'pricebook']:
    df = pd.read_sql_query(f'SELECT * FROM {table}', conn)
    duplicates = df[df.duplicated()]
    if not duplicates.empty:
        log_issue(table, 'Duplicate', f'Found {len(duplicates)} duplicate rows.')
        print(f"⚠️ Duplicates found in {table}: {len(duplicates)} rows.")
    else:
        print(f"✅ No duplicates found in {table}.")
        log_issue(table, 'No Duplicate', 'No duplicate rows found.')

# Nulls in key fields
print("🔍 Checking for nulls in key fields...")
key_fields = {
    'customers': 'customer_id',
    'vendors': 'vendor_id',
    'items': 'item_id',
    'pricebook': 'item_id'
}
for table, key in key_fields.items():
    df = pd.read_sql_query(f'SELECT * FROM {table}', conn)
    nulls = df[df[key].isnull()]
    if not nulls.empty:
        log_issue(table, 'Null Key Field', f'Found {len(nulls)} rows with null {key}.')
        print(f"⚠️ Nulls found in {table} ({key}): {len(nulls)} rows.")
    else:
        print(f"✅ No nulls found in {table} ({key}).")
        log_issue(table, 'No Null Key Field', f'No null {key} found.')

# Inconsistent pricing
print("🔍 Checking for excessive discounts...")
cursor.execute('SELECT COUNT(*) FROM pricebook WHERE discount > 0.9')
count = cursor.fetchone()[0]
if count > 0:
    log_issue('pricebook', 'Excessive Discount', f'Found {count} rows with discount > 90%.')
    print(f"⚠️ Excessive discounts found in pricebook: {count} rows.")
else:
    print("✅ No excessive discounts found in pricebook.")
    log_issue('pricebook', 'No Excessive Discount', 'No excessive discounts found.')

# Unlinked foreign keys
print("🔍 Checking for unlinked foreign keys...")
cursor.execute('SELECT COUNT(*) FROM items WHERE vendor_id NOT IN (SELECT vendor_id FROM vendors)')
count = cursor.fetchone()[0]
if count > 0:
    log_issue('items', 'Unlinked Foreign Key', f'Found {count} items with unlinked vendor_id.')
    print(f"⚠️ Unlinked foreign keys found in items: {count} rows.")
else:
    print("✅ No unlinked foreign keys found in items.")
    log_issue('items', 'No Unlinked Foreign Key', 'All vendor_ids are linked to vendors.')

# Commit and close
conn.commit()
conn.close()
print("✅ Audit log created and issues logged.")
