
# Set a base docker image (see https://hub.docker.com/)
FROM python:3.9-slim

# Name of the maintainer 
MAINTAINER Niklas Lang

# 2. (optional) use python wheels from piwheels.org (speeds up build time for arm architectures)
RUN echo '[global]' > /etc/pip.conf && echo 'extra-index-url=https://www.piwheels.org/simple' >> /etc/pip.conf

# Install / Update Raspbian dependencies
RUN apt update && apt install -y \
    python3-pip

# Update pip
RUN pip3 install --upgrade pip

COPY requirements.txt ./requirements.txt

# Install python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

RUN mkdir /app

WORKDIR /app

# Copy the data to root folder
COPY . ./

# Run the script
CMD ["python3", "-u", "data_logger.py"]

