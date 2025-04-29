from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from datetime import datetime, timedelta
import duckdb

# Selenium setup
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get("https://data.nordpoolgroup.com/auction/day-ahead/price-indices?deliveryDate=latest&currency=EUR&resolutionInMinutes=15&indexNames=LV")
time.sleep(6)

# Scrape prices
rows = driver.find_elements(By.CSS_SELECTOR, '.dx-data-row')
data = []

# Today's and tomorrow's date
today = datetime.now()
today_str = today.strftime("%d-%m-%Y")
tomorrow_str = (today + timedelta(days=1)).strftime("%d-%m-%Y")
# If you use the script after 14:00, uncomment after_tomorrow_str
after_tomorrow_str = (today + timedelta(days=2)).strftime("%d-%m-%Y")

for row in rows:
    cells = row.find_elements(By.TAG_NAME, 'td')
    if len(cells) >= 2:
        full_period = cells[0].text.strip()
        period_start = full_period.split(" - ")[0]
        price = cells[1].text.strip().replace(",", ".")

        # Change '00:' times to '24:' and update the delivery date to the next day
        if period_start.startswith("00:"):
            # period_start = "24:" + period_start[3:]  # Change '00:' to '24:'
            # Update to the next day
            delivery_date = after_tomorrow_str  # Change after_tomorrow_str or tomorrow_str
        else:
            delivery_date = tomorrow_str  # Change tomorrow_str or today_str

        price_value = float(price)
        data.append([delivery_date, period_start, price_value])

# Connect to DuckDB
conn = duckdb.connect(
    database='/Users/wolf/Documents/GitHub/nordpool/prices.duckdb', read_only=False)

# Create the table if it doesn't exist
conn.execute("""
    CREATE TABLE IF NOT EXISTS latvia_prices (
        Date TEXT,
        Delivery_Period TEXT,
        Price_EUR_MWh DOUBLE
    )
""")

# Check if data for the current date and delivery period already exists
for row in data:
    date = row[0]
    period = row[1]
    # Query to check if this specific date and period already exists
    query = f"SELECT COUNT(*) FROM latvia_prices WHERE Date = '{date}' AND Delivery_Period = '{period}'"
    existing_data = conn.execute(query).fetchone()

    if existing_data[0] == 0:
        # If no existing data, insert the new record
        conn.execute(
            "INSERT INTO latvia_prices (Date, Delivery_Period, Price_EUR_MWh) VALUES (?, ?, ?)", row)
        print(f"Inserted data: {row}")
    else:
        print(
            f"Data for {date} at {period} already exists, skipping insertion.")

# Close the connection to the database
conn.close()
