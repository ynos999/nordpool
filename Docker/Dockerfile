# Use the official Python base image for ARM64
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install necessary system packages (including Chromium)
RUN apt-get clean && apt-get update && \
    apt-get install -y \
    cron \
    vim \
    python3-pip \
    tzdata \
    unzip \
    wget \
    gnupg \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Set Chromium binary and driver paths (explicitly for ARM64)
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROME_DRIVER_PATH=/usr/bin/chromedriver

# Copy your Python scripts and requirements.txt into the container
COPY ./scripts /app
COPY ./requirements.txt /app
COPY ./prices.duckdb /app
COPY ./.env /app

# Set the timezone to Europe/Riga
RUN ln -sf /usr/share/zoneinfo/Europe/Riga /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# Add the crontab file and ensure the last line ends with a newline
COPY crontab /etc/cron.d/tasmota-cron

# Ensure proper permissions and ensure the crontab file is valid
RUN chmod 0644 /etc/cron.d/tasmota-cron && \
    echo '' >> /etc/cron.d/tasmota-cron && \
    crontab /etc/cron.d/tasmota-cron

# Create the log file to track cron jobs
RUN touch /var/log/cron.log

# Install Python dependencies
RUN ln -s /usr/bin/python3 /usr/bin/python && \
    pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r /app/requirements.txt

# Set display port to avoid crash (for Selenium)
ENV DISPLAY=:99

# Start cron in the background and tail the cron logs
CMD ["sh", "-c", "service cron start && tail -f /var/log/cron.log"]