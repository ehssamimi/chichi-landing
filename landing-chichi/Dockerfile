#FROM node:8
#
#RUN mkdir app
#EXPOSE 3000
#
#COPY . ./app
#
#WORKDIR app
#
#RUN npm install
#
#CMD [ "npm","start"]

#
#FROM node:12.2.0-alpine as build
#WORKDIR /app
#ENV PATH /app/node_modules/.bin:$PATH
#COPY package.json /app/package.json
#RUN npm install --silent
#RUN npm install react-scripts@3.0.1 -g --silent
#COPY . /app
#RUN npm run build
#
## production environment
#FROM nginx:1.16.0-alpine
#COPY --from=build /app/build /usr/share/nginx/html
#EXPOSE 80
#CMD ["nginx", "-g", "daemon off;"]


FROM nginx:alpine
COPY default.conf /etc/nginx/conf.d/default.conf
COPY landpage.html /usr/share/nginx/html/index.html
COPY . /usr/share/nginx/html/