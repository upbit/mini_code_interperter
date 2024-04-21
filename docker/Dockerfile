# Use the official Python 3.10 image as the base image  
FROM python:3.10-slim

RUN apt update && apt install -y gcc

COPY requirements.txt /
RUN python3 -m pip install --no-cache-dir --upgrade pip wheel
RUN python3 -m pip install --no-cache-dir --no-warn-script-location -r /requirements.txt && \
    rm -vf /requirements.txt

WORKDIR /app

# Copy the project code
COPY kernel/ /app/kernel/
COPY docker/entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENV PYTHONPATH "${PYTHONPATH}:/app"

ENTRYPOINT ["/app/entrypoint.sh"]