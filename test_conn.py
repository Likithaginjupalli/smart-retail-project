print("🚀 Script started")

from sqlalchemy import create_engine

try:
    engine = create_engine("postgresql+psycopg2://postgres:postgres2930@localhost:5432/retail_dw")
    conn = engine.connect()
    print("✅ Connection successful!")
    conn.close()
except Exception as e:
    print("❌ Connection failed:")
    print(e)

