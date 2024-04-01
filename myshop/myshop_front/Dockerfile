FROM node:21.7.1-alpine as builder

ENV NODE_ENV=production
ENV PATH /usr/src/node_modules/.bin:$PATH

ARG VITE_BACKEND_URL

ENV VITE_BACKEND_URL=$VITE_BACKEND_URL

WORKDIR /usr/app/

COPY package*.json ./
RUN npm install

COPY . ./

RUN npm run build
