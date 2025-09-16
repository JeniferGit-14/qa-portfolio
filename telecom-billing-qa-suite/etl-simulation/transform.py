import pandas as pd

# Read raw billing data
raw = pd.DataFrame({
    'customer_id': [1, 2, 3],
    'bill_amount': [100, 200, 150],
    'is_late': [0, 1, 1]
})

# Apply transformation (add late fee)
raw['final_amount'] = raw['bill_amount'] + raw['is_late'] * 20

# Save to CSV (simulating ETL)
raw.to_csv('transformed_billing.csv', index=False)
print('ETL Transformation complete. Output saved to transformed_billing.csv')
