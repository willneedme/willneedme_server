FROM node:14-alpine

WORKDIR /usr/src/node
COPY package-lock.json /usr/src/node
COPY package.json /usr/src/node
RUN npm install

COPY . /usr/src/node
RUN npm install -g nodemon --no-optional
CMD ["nodemon","server.js" ]