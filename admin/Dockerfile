FROM node:14.15.4


WORKDIR /usr/src/app
ENV PATH /usr/src/app/node_modules/.bin:$PATH

COPY package.json /usr/src/app
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm","start"]