from datetime import datetime, timedelta
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver


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
            delivery_date = after_tomorrow_str   # tomorrow_str If you use script after 14:00
        else:
            delivery_date = tomorrow_str      # today_str If you use script after 14:00

        price_value = float(price)
        data.append([delivery_date, period, price_value])

        if price_value < min_price:
            min_price = price_value
            min_time = period

# Print the lowest price and corresponding time
print(f"Lowest Price: {min_price} EUR/MWh at Time: {min_time}")

# Create a DataFrame
df = pd.DataFrame(
    data, columns=["Date", "Delivery Period (EET)", "Price (EUR/MWh)"])

# Save the DataFrame as CSV
filename = f"LV_price_15_tomorrow_{tomorrow_str}.csv"
df.to_csv(filename, index=False)
print(f"Data saved to {filename}")

# Close the WebDriver
driver.quit()
