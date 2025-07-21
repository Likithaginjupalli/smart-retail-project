import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart Retail Dashboard")

st.title("📊 Smart Retail Dashboard")

# Load the CSV generated earlier
df = pd.read_csv('data_products/sales_summary.csv')


st.subheader("Sales Summary")
st.dataframe(df)

# Optional: Basic chart
st.subheader("Total Quantity Sold per Product")
st.bar_chart(df.set_index('product_id')['total_qty'])

st.subheader("Revenue by Product")
st.bar_chart(df.set_index('product_id')['revenue'])
