import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

NUM_CUSTOMERS = 100
NUM_VENDORS = 20
NUM_ITEMS = 50
CUSTOMER_TYPES = ['Retail', 'Wholesale']
VENDOR_CATEGORIES = ['Electronics', 'Clothing', 'Food', 'Office Supplies']

# Customers
customers = pd.DataFrame({
    'customer_id': range(1, NUM_CUSTOMERS + 1),
    'customer_name': [fake.company() for _ in range(NUM_CUSTOMERS)],
    'region': [fake.state() for _ in range(NUM_CUSTOMERS)],
    'customer_type': [random.choice(CUSTOMER_TYPES) for _ in range(NUM_CUSTOMERS)]
})

# Vendors
vendors = pd.DataFrame({
    'vendor_id': range(1, NUM_VENDORS + 1),
    'vendor_name': [fake.company() for _ in range(NUM_VENDORS)],
    'region': [fake.state() for _ in range(NUM_VENDORS)],
    'category': [random.choice(VENDOR_CATEGORIES) for _ in range(NUM_VENDORS)],
    'status': [random.choice(['Active', 'Inactive']) for _ in range(NUM_VENDORS)]
})

# Items
items = pd.DataFrame({
    'item_id': range(1, NUM_ITEMS + 1),
    'item_description': [fake.bs().title() for _ in range(NUM_ITEMS)],
    'vendor_id': [random.randint(1, NUM_VENDORS) for _ in range(NUM_ITEMS)],
    'unit_cost': np.round(np.random.uniform(5, 100, NUM_ITEMS), 2)
})

# Pricebook
pricebook = []
for item_id in range(1, NUM_ITEMS + 1):
    for ctype in CUSTOMER_TYPES:
        list_price = round(items.loc[item_id - 1, 'unit_cost'] * random.uniform(1.1, 1.5), 2)
        discount = round(random.uniform(0, 0.2), 2)
        pricebook.append({
            'item_id': item_id,
            'customer_type': ctype,
            'list_price': list_price,
            'discount': discount
        })

pricebook = pd.DataFrame(pricebook)

# Introduce some data issues (for cleaning later)
# Duplicates
customers = pd.concat([customers, customers.sample(5, random_state=1)])
# Nulls
vendors.loc[vendors.sample(2).index, 'region'] = None
items.loc[items.sample(2).index, 'vendor_id'] = None

# Export to CSV
customers.to_csv('customers.csv', index=False)
vendors.to_csv('vendors.csv', index=False)
items.to_csv('items.csv', index=False)
pricebook.to_csv('pricebook.csv', index=False)

print("✅ Simulated ERP data saved to CSVs.")
