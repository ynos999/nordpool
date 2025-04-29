from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from datetime import datetime, timedelta

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get("https://data.nordpoolgroup.com/auction/day-ahead/prices?deliveryDate=latest&currency=EUR&aggregation=DeliveryPeriod&deliveryAreas=LV")
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
            delivery_date = tomorrow_str  # Change after_tomorrow_str if use script after 14:00
        else:
            delivery_date = today_str  # Change tomorrow_str if use script after 14:00

        price_value = float(price)
        data.append([delivery_date, period_start, price_value])

# Print the lowest price and corresponding time
print(f"Lowest Price: {min_price} EUR/MWh at Time: {min_time}")

# Create a DataFrame
df = pd.DataFrame(
    data, columns=["Date", "Delivery Period (EET)", "Price (EUR/MWh)"])

# Save the DataFrame as CSV
filename = f"LV_price_{today_str}.csv"
df.to_csv(filename, index=False)
print(f"Data saved to {filename}")

# Close the WebDriver
driver.quit()
