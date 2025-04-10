# Nordpool LV Price today or tomorrow
###
###
## The script collects data from Nordpool for Latvia, current day and saves it to a csv file.
###
### Manual for Linux and MAC OSX:
###
### python3 -m pip install virtualenv
### python3 -m venv .venv
### source .venv/bin/activate
### pip install -r requirements.txt
### pip install --upgrade pip
### python nordpool_1h.py or python3 nordpool_1h.py
###
### Output: 
### Lowest Price: 3.44 EUR/MWh at Time: 15:00 and data saved to LV_price_10-04-2025.csv
###
### For deactivate venv:
###
### conda deactivate
###
### If You use script after 12:00 or need data for next day, modificate skript.
### Uncomment after_tomorrow_str and change:
###
### delivery_date = after_tomorrow_str  
### delivery_date = tomorrow_str
###
###
###  When SDAC 15-minute goes live, estimated for 11 June 2025, official Day-Ahead prices will be provided in 15-minute resolution. This update is mandated externally and is not within our control.

### For users who require different resolutions, Nord Pool has introduced normalized price indices for a set resolution.

### The change only applies to delivery dates after go-live date. For example, if SDAC go-live date is on 11 June 2025, the prices will be updated in 15-minute resolution after the auction run on 11 June, for delivery on 12 June 2025 (starting with the 00:00-00:15 CET contract period). 
###
###
### New link:
### https://data.nordpoolgroup.com/auction/day-ahead/price-indices?deliveryDate=latest&currency=EUR&resolutionInMinutes=15&indexNames=LV
###
###
### python nordpool_15m.py or python3 nordpool_15m.py