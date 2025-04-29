import duckdb
from datetime import datetime

# Get today's date
today = datetime.now()
print("Today:", today)
today_str = today.strftime("%d-%m-%Y")  # Format the date as day-month-year
print("Today:", today_str)

# Print today's date
print("Today:", today)

# Connect to DuckDB
conn = duckdb.connect('/Users/wolf/Documents/GitHub/nordpool/prices.duckdb')

# Query to select all rows for today's date
query = f"SELECT * FROM latvia_prices WHERE Date = '{today_str}'"

# Execute the query and fetch all results
query_result = conn.execute(query).fetchall()

# Check if there are results
if query_result:
    print(f"Data for {today_str}:")
    for row in query_result:
        # row = (Date, Delivery_Period, Price_EUR_MWh)
        print(f"Date: {row[0]}, Time: {row[1]}, Price: {row[2]} EUR/MWh")
else:
    print(f"No data found for {today_str}")

# Close the connection
conn.close()
