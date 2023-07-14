# Pull base image
FROM python:3.9

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY app /app/
COPY app/configs /app/
COPY app/unittests /app/
COPY app/db_migrations /app/
COPY app/main.py /app/
COPY requirements.txt /app/

# Install dependencies
RUN pip install -r /app/requirements.txt

EXPOSE 8000
ENTRYPOINT["/bin/sh"]