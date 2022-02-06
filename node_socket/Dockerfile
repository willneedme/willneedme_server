FROM node:14-alpine

WORKDIR /usr/src/node_socket
COPY package-lock.json /usr/src/node_socket
COPY package.json /usr/src/node_socket
RUN npm install

COPY . /usr/src/node_socket
RUN npm install -g nodemon --no-optional
CMD [ "nodemon", "server.js" ]