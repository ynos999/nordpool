import duckdb
from datetime import datetime, timedelta

today = datetime.now()
today_str = today.strftime("%d-%m-%Y")
# Define the date you want to filter (e.g., today) + 1 day
target_date = (today + timedelta(days=1)).strftime("%d-%m-%Y")

# Connect to DuckDB
conn = duckdb.connect('prices.duckdb')  # My database file name (prices.duckdb)

# Optional: List all tables
tables = conn.execute("SHOW TABLES").fetchall()
print("Tables:", tables)

# Query only rows for the target date

# Change if neead to target_date
# Change if neead to today_str
query = f"SELECT * FROM latvia_prices WHERE Date = '{target_date}'"
query_result = conn.execute(query).fetchall()

print(f"Rows for {today_str}:", query_result)  # Change if neead to today_str

# Close the connection
conn.close()
