import pandas as pd

# Step 1: Load raw data
df = pd.read_csv('./data_lake/raw/in_store_sales.csv')

# Step 2: Clean data
df_clean = df.dropna().drop_duplicates()

# Step 3: Save to curated layer
df_clean.to_csv('./data_lake/curated/in_store_sales_clean.csv', index=False)

print("✅ In-store sales data cleaned and saved!")
