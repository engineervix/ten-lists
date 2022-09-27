FROM node:14.20.0-bullseye

# RUN useradd flask
WORKDIR /usr/src/app

# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY ./package*.json  /usr/src/app

RUN npm ci

ENV PATH ./node_modules/.bin/:$PATH

# ENTRYPOINT ["/usr/src/app/docker/node/entrypoint.sh"]
