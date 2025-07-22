![Smart Retail Dashboard](./smart-retail-banner.png)
# 🛍️ Smart Retail Data Pipeline & Dashboard

This project simulates a **retail sales pipeline** using CSV data, PostgreSQL for warehousing, and **Streamlit** for visual analytics.

---

## 🗂️ Project Structure

```yaml
name: Smart Retail Project
version: 1.0
dependencies:
  - pandas
  - sqlalchemy
  - psycopg2
  - streamlit
database:
  name: retail_dw
  user: postgres
  password: postgres2930

```bash
smart-retail-project/
├── data/                  # Raw input CSV files (e.g., sales.csv)
├── data_products/         # Output folder (e.g., sales_summary.csv)
├── dashboard/
│   └── dashboard.py       # Streamlit dashboard UI logic
├── data_mesh/
│   └── sales/
│       └── sales_summary.py  # ETL logic to summarize data
├── load_to_dw.py          # Loads raw data into PostgreSQL
├── requirements.txt       # Python packages list
└── README.md              # Project description
