import duckdb
from datetime import datetime

# Connect to DuckDB
conn = duckdb.connect('/Users/wolf/Documents/GitHub/nordpool/prices.duckdb')

select_query = "SELECT * FROM latvia_prices"
select_result = conn.execute(select_query).fetchall()

print("Preview of 'latvia_prices' table:")
for row in select_result:
    print(row)

# Close the connection
conn.close()
