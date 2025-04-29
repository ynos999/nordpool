## Nordpool LV Price today or tomorrow
###
### The script collects data from Nordpool for Latvia, current day and saves it to a csv file.
###
#### Manual for Linux and MAC OSX:
###
#### python3 -m pip install virtualenv
#### python3 -m venv .venv
#### source .venv/bin/activate
#### pip or pip3...
#### pip install -r requirements.txt
#### pip install --upgrade pip
###
### Print this day Nordpool data if you start script until 12:00.
###
### python nordpool_1h.py or python3 nordpool_1h.py
###
##### Output: 
##### Lowest Price: 3.44 EUR/MWh at Time: 15:00 and data saved to LV_price_10-04-2025.csv
###
### For deactivate venv:
###
### conda deactivate
###
### If You use script after 14:00 or need data for next day, modificate skript or use *_next_d.py.
###
### 15. min. period from Nordpoll save to duckdb.
###
#### python nordpool_15m_db.py
###
### Print duckdb database Nordpool data.
###
#### python dbduck_print_....py
###
### Next day from Nordpoll. Start script after 14:00.
### Create csv file.
#### python nordpool_15m_next_d.py
### Create csv file and iport data to database. Start script after 14:00.
#### python nordpool_15m_db_next_d.py
### Print duckdb database next day Nordpool data.
#### python dbduck_print_next_d.py

# TASMOTA AND NORDPOOL LV
## TEST WITH SONOFF BASIC R4 AND TASMOTA.
### 1. STEP. ADD TO DATABASE DATA. RUN python tasmota_db_write_next_day_15m.py or nordpool_15m_db.py
## 
## READ and TURN ON OR OFF TASMOTA SONOFF.
### 2. STEP change YOUR SONOFF IP, User AND Password in file tasmota_db_read.py.
### Tasmota data:
### TASMOTA_IP = "YOUR IP"
### USER = "YOUR USER"
### PASSWORD = "YOUR PASSWORD"
### 3. STEP. RUN python tasmota_db_read.py
### 4. Crontab add (change to your location):
### 0 16,20,21 * * * /usr/local/bin/python3.13 /YOUR_LOCATION/nordpool/tasmota_db_write_next_day_15m.py
### */5 * * * * /usr/local/bin/python3.13 /YOUR_LOCATION/tasmota_db_read.py
##
## DOCKER
### Create .env file in Docker folder, befor use docker.
### RUN:
### docker build -t tasmota-cron-job .
### docker build --no-cache -t tasmota-cron-job .
### docker run -d --name tasmota-cron-job tasmota-cron-job
### docker logs -f tasmota-cron-job
### docker exec -it tasmota-cron-job date
### DON'T work with arm64 processors.