import pandas as pd
from sqlalchemy import create_engine

# Step 1: Read CSV
df = pd.read_csv('./data_lake/curated/in_store_sales_clean.csv')

# Step 2: Rename columns to match DB table
df.rename(columns={
    'StoreID': 'store_id',
    'Product': 'product_id',   # assuming Product is product_id
    'Quantity': 'quantity',
    'Price': 'price'
}, inplace=True)

# Optional: Add dummy date column if needed
df['date'] = pd.Timestamp.today().normalize()  # use today's date

# Step 3: Connect to PostgreSQL
engine = create_engine("postgresql+psycopg2://postgres:postgres2930@localhost:5432/retail_dw")

# Step 4: Load to table
df.to_sql('fact_sales', con=engine, if_exists='append', index=False)

print("✅ Data loaded into Data Warehouse!")
