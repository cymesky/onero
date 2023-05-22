# install python
FROM python:3.10

# set workdir
WORKDIR /opt/scrapy_service

# copy files
COPY requirements.txt .
COPY app.py .

# install requirements modules
RUN pip install --no-cache-dir -r requirements.txt

# copy our spider
COPY spiders/ ./spiders/

# set environment
ENV PYTHONPATH=/opt/scrapy_service/app

# Copy crontab to container
COPY crontab /etc/cron.d/scrapy-cron-job

# Install cron
RUN apt-get update && apt-get install -y cron

# Rights for cronjob
RUN chmod 0644 /etc/cron.d/scrapy-cron-job

# enable logs for cron
RUN touch /var/log/cron.log

# start scrapy service and cron
CMD cron && python /opt/scrapy_service/app.py >> /var/log/cron.log 2>&1 && tail -f /var/log/cron.log
