### Nordpool LV Price today or tomorrow
###
###
### The script collects data from Nordpool for Latvia, current day and saves it to a csv file.
###
### Manual for Linux and MAC OSX:
###
### python3 -m pip install virtualenv
### python3 -m venv .venv
### source .venv/bin/activate
### pip install -r requirements.txt
### pip install --upgrade pip
### python main.py or python3 main.py
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