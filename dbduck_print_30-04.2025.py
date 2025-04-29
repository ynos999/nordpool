import duckdb
from datetime import datetime

# Connect to DuckDB
conn = duckdb.connect('/Users/wolf/Documents/GitHub/nordpool/prices.duckdb')

# Query to select all rows for 29-04-2025
query = "SELECT * FROM latvia_prices WHERE Date = '30-04-2025'"

# Execute the query and fetch all results
query_result = conn.execute(query).fetchall()

# Check if there are results
if query_result:
    print("Data for 30-04-2025:")
    for row in query_result:
        # row = (Date, Delivery_Period, Price_EUR_MWh)
        print(f"Date: {row[0]}, Time: {row[1]}, Price: {row[2]} EUR/MWh")
else:
    print("No data found for 30-04-2025")

# Close the connection
conn.close()
