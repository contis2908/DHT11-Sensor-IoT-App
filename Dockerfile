
# 1. Set a base docker image (see https://hub.docker.com/)
FROM node:current-alpine

# 4. Copy settings file to image
COPY package.json ./

# 5. Update / Install app dependencies listed in package.json
RUN npm install

# 6. Copy the app code
COPY . ./

# 8. Run the application
CMD [ "node", "/index.js" ]
