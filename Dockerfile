#################################################################################
# use node:14-bookworm as the base image for building the frontend
#################################################################################

FROM node:14-bookworm AS frontend-builder

# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json Gruntfile.js ./
RUN npm ci --no-optional --no-audit --progress=false --network=host

COPY ./tenlists/webapp/ten_lists/static/ ./tenlists/webapp/ten_lists/static/
RUN npm run build

#################################################################################
# use python:3.12-slim-bookworm as the base image for production and development
#################################################################################

FROM python:3.12-slim-bookworm AS production

# Add user that will be used in the container
RUN groupadd flask && \
    useradd --create-home --shell /bin/bash -g flask flask

RUN mkdir -p /home/flask/app && chown flask:flask /home/flask/app

# set work directory
WORKDIR /home/flask/app

# Port used by this container to serve HTTP.
EXPOSE 8000

# set environment variables
# - Force Python stdout and stderr streams to be unbuffered.
# - Set PORT variable that is used by Gunicorn. This should match "EXPOSE" command.
ENV PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONPATH=/home/flask/app \
    WEB_CONCURRENCY=3 \
    PORT=8000 \
    FLASK_CONFIGURATION=production \
    FLASK_ENV=production

# Install system dependencies
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    curl \
    ffmpeg \
    git \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Use user "flask" to run the build commands below and the server itself.
USER flask

# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY ./package*.json  /home/flask/app/
RUN npm ci

# install python dependencies
ENV VIRTUAL_ENV=/home/flask/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install --upgrade pip
COPY --chown=flask ./requirements.txt .
RUN pip install -r requirements.txt

# Copy build artifacts from frontend-builder stage
COPY --from=frontend-builder --chown=flask:flask /tenlists/webapp/ten_lists/static/css/custom.min.css /home/flask/app/tenlists/webapp/ten_lists/static/css/custom.min.css
COPY --from=frontend-builder --chown=flask:flask /tenlists/webapp/ten_lists/static/js/custom.min.js /home/flask/app/tenlists/webapp/ten_lists/static/js/custom.min.js
COPY --from=frontend-builder --chown=flask:flask /tenlists/webapp/ten_lists/static/vendors /home/flask/app/tenlists/webapp/ten_lists/static/vendors

# Copy the source code of the project into the container
COPY --chown=flask:flask . .

# Runtime command that executes when "docker run" is called
CMD "gunicorn tenlists.webapp.ten_lists:create_app()"


#################################################################################
# The next steps won't be run in production
#################################################################################

FROM production AS dev

# Swap user, so the following tasks can be run as root
USER root

# set environment variables
ENV NODE_MAJOR=14 \
    PATH=/home/flask/app/node_modules/.bin:$PATH

# Install node (Keep the version in sync with the node container above)
RUN curl -fsSL https://deb.nodesource.com/setup_${NODE_MAJOR}.x | bash - && \
    apt-get install -y nodejs
RUN npm install -g grunt-cli

# Restore user
USER flask

# Pull in the node modules for the frontend
COPY --chown=flask:flask --from=frontend-builder ./node_modules ./node_modules

# do nothing - exec commands elsewhere
CMD tail -f /dev/null
