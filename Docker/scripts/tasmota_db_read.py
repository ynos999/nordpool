import os
import duckdb
from datetime import datetime
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv(dotenv_path='/app/.env')


# Read environment variables
TASMOTA_IP = os.getenv("TASMOTA_IP")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")


def send_tasmota_command(power_state):
    url = f"http://{TASMOTA_IP}/cm"
    params = {
        "user": USER,
        "password": PASSWORD,
        "cmnd": f"Power {power_state}"
    }
    try:
        response = requests.get(url, params=params, timeout=5)
        print(f"Sent to Power {power_state} command. Answer: {response.text}")
    except Exception as e:
        print(f"Error sending command to Tasmota: {e}")


# Get the current time
today = datetime.now()
print("Today:", today)
today_str = today.strftime("%d-%m-%Y")

# Connect to DuckDB
conn = duckdb.connect('/app/prices.duckdb')

# Query to select rows for the current date
query = f"SELECT * FROM latvia_prices WHERE Date = '{today_str}'"
query_result = conn.execute(query).fetchall()

# Check if we got any result
if query_result:
    # Get the current time and round it to the nearest 15-minute period
    current_time = today.strftime("%H:%M")  # e.g., '10:12'

    # Round to the nearest 15-minute period
    # Get the minute part of current time
    current_minute = int(today.strftime("%M"))

    if current_minute < 15:
        nearest_time = f"{today.strftime('%H')}:00"  # Closest on the hour
    elif current_minute < 30:
        # Closest at the 15-minute mark
        nearest_time = f"{today.strftime('%H')}:15"
    elif current_minute < 45:
        # Closest at the 30-minute mark
        nearest_time = f"{today.strftime('%H')}:30"
    else:
        # Closest at the 45-minute mark
        nearest_time = f"{today.strftime('%H')}:45"

    print(
        f"Nearest time period to the current time ({current_time}) is {nearest_time}")

    # Loop through the query result and find the price for the nearest time
    for row in query_result:
        # row = (Date, Delivery_Period, Price_EUR_MWh)
        # This is the 'Delivery Period' (e.g., '08:00')
        delivery_period = row[1]
        price = row[2]  # This is the price in EUR/MWh

        # Check if the delivery period matches the nearest time
        if delivery_period == nearest_time:
            print(f"Current price at {nearest_time}: {price} EUR/MWh")

            # Control Tasmota based on the price
            if price > 25:
                send_tasmota_command("Off")
            else:
                send_tasmota_command("On")
            break  # We found the right row, no need to continue looping
else:
    print(f"No data found for {today_str}")

# Close the connection
conn.close()
