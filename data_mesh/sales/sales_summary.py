import pandas as pd
from sqlalchemy import create_engine

# Connect to PostgreSQL
engine = create_engine('postgresql://postgres:postgres2930@localhost:5432/retail_dw')

# SQL query to generate sales summary
query = """
SELECT 
    product_id, 
    SUM(quantity) AS total_qty, 
    SUM(price * quantity) AS revenue 
FROM fact_sales 
GROUP BY product_id
"""

# Read SQL output into DataFrame
df = pd.read_sql(query, engine)

# Save the result to a CSV
df.to_csv('./data_products/sales_summary.csv', index=False)

print("✅ Sales summary data product created.")
