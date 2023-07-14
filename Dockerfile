# Pull base image
FROM python:3.9

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /
COPY . /

# Install dependencies
RUN pip install -r /requirements.txt

EXPOSE 8000
#ENTRYPOINT["/bin/sh"]