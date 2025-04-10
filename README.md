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
### pip or pip3...
### pip install -r requirements.txt
### pip install --upgrade pip
###
### Print this day Nordpool data if you start script until 12:00.
###
### python nordpool_1h.py or python3 nordpool_1h.py
###
### Output: 
### Lowest Price: 3.44 EUR/MWh at Time: 15:00 and data saved to LV_price_10-04-2025.csv
###
### For deactivate venv:
###
### conda deactivate
###
### If You use script after 14:00 or need data for next day, modificate skript.
### Uncomment after_tomorrow_str and change:
###
### delivery_date = after_tomorrow_str  
### delivery_date = tomorrow_str
###
#####  When SDAC 15-minute goes live, estimated for 11 June 2025, official Day-Ahead prices will be provided in 15-minute resolution. This update is mandated externally and is not within our control.
### The change only applies to delivery dates after go-live date. For example, if SDAC go-live date is on 11 June 2025, the prices will be updated in 15-minute resolution after the auction run on 11 June, for delivery on 12 June 2025 (starting with the 00:00-00:15 CET contract period). 
###
## 15. min. period this day data from Nordpoll. Start script until 14:00.
###
### python nordpool_15m.py or python3 nordpool_15m.py
###
## 15. min. period from Nordpoll save to duckdb.
###
### python nordpool_15m_db.py
###
## Print duckdb database Nordpool data.
###
### python dbduck_print.py
###
### Next day from Nordpoll. Start script after 14:00.
### Create csv file.
### nordpool_15m_next_d.py
### Create csv file and iport data to database. Start script after 14:00.
### nordpool_15m_db_next_d.py
### Print duckdb database next day Nordpool data.
### dbduck_print_next_d.py