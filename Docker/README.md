docker build -t tasmota-cron-job .
docker build --no-cache -t tasmota-cron-job .
docker run -d --name tasmota-cron-job tasmota-cron-job
docker logs -f tasmota-cron-job
docker exec -it tasmota-cron-job date

docker exec -it tasmota-cron-job sh
pip3 install --no-cache-dir -r /app/requirements.txt
pip3 install --upgrade pip
python tasmota_db_write_next_day_15m.py
