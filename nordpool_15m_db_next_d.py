from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from datetime import datetime, timedelta
import duckdb


options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get("https://data.nordpoolgroup.com/auction/day-ahead/price-indices?deliveryDate=latest&currency=EUR&resolutionInMinutes=15&indexNames=LV")
time.sleep(6)

# Scraping the data
# Class name .dx-data-row
rows = driver.find_elements(By.CSS_SELECTOR, '.dx-data-row')
data = []
min_price = float('inf')
min_time = ""

# Today's and tomorrow's date
today = datetime.now()
today_str = today.strftime("%d-%m-%Y")
tomorrow_str = (today + timedelta(days=1)).strftime("%d-%m-%Y")
# If you use script after 14:00 uncomment after_tomorrow_str
after_tomorrow_str = (today + timedelta(days=2)).strftime("%d-%m-%Y")

for row in rows:
    cells = row.find_elements(By.TAG_NAME, 'td')
    if len(cells) >= 2:
        full_period = cells[0].text.strip()
        period = full_period.split(" - ")[0]  # Get only the start time
        # period = cells[0].text.strip()
        price = cells[1].text.strip().replace(",", ".")

        # Assign correct date
        if period.startswith("00:"):
            # after_tomorrow_str If you use script after 14:00
            delivery_date = after_tomorrow_str  # after_tomorrow_str
        else:
            delivery_date = tomorrow_str  # tomorrow_str
            # tomorrow_str If you use script after 14:00

        price_value = float(price)
        data.append([delivery_date, period, price_value])

        if price_value < min_price:
            min_price = price_value
            min_time = period

# Print the lowest price and corresponding time
# print(f"Lowest Price: {min_price} EUR/MWh at Time: {min_time}")

# Create a DataFrame
df = pd.DataFrame(
    data, columns=["Date", "Delivery Period (EET)", "Price (EUR/MWh)"])

# Save the DataFrame as CSV
filename = f"LV_price_db_{tomorrow_str}.csv"  # Change if neead to tomorrow_str
df.to_csv(filename, index=False)
print(f"Data saved to {filename}")

# Save the data to DuckDB
conn = duckdb.connect(database='prices.duckdb', read_only=False)
conn.execute("""
    CREATE TABLE IF NOT EXISTS latvia_prices (
        Date TEXT,
        Delivery_Period TEXT,
        Price_EUR_MWh DOUBLE
    )
""")
conn.executemany(
    "INSERT INTO latvia_prices (Date, Delivery_Period, Price_EUR_MWh) VALUES (?, ?, ?)", data)
conn.close()

# Close the WebDriver
driver.quit()
