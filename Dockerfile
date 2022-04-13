
# 1. Set a base docker image (see https://hub.docker.com/)
# FROM node:current-alpine
FROM raspbian/stretch

# 2. Name of the maintainer 
MAINTAINER Niklas Lang

# 3. Install / Update Raspbian dependencies
RUN apt update && apt install -y python3-dev \
    python3-pip
    # curl \
    # git \

# 4. Update setup tools
RUN pip3 install --upgrade setuptools 

# 5. Install python dependencies
RUN pip3 install Adafruit_DHT

# 8. Install / Update Autobahn and other crossbar related dependencies
RUN pip3 install \
    # requests \
    autobahn \
    twisted \
    # cryptography \
    cbor

# 9. Copy the data to root folder
COPY . ./

# 10. Run the script
CMD ["python3", "/data_logger.py"]



