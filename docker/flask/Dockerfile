FROM python:3.8-slim-bullseye

# Add user that will be used in the container
RUN groupadd flask && \
    useradd --create-home --shell /bin/bash -g flask flask

RUN mkdir -p /home/flask/app && chown flask:flask /home/flask/app

# set work directory
WORKDIR /home/flask/app

# Port used by this container to serve HTTP.
EXPOSE 5000

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=5000 \
    PATH=/home/flask/app/node_modules/.bin:$PATH

# install system dependencies
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    curl \
    git \
    libjpeg62-turbo-dev \
    libmariadb-dev-compat libmariadb-dev \
    libpq-dev \
    libwebp-dev \
    zlib1g-dev \
    && apt-get clean

# install Node.js
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt install nodejs -y

# Don't use the root user as it's an anti-pattern
USER flask

# install python dependencies
ENV VIRTUAL_ENV=/home/flask/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install --upgrade pip
COPY --chown=flask ./requirements.txt .
RUN pip install -r requirements.txt

# node dependencies
# RUN npm ci

COPY --chown=flask . .

# Generate static assets
# RUN gulp cp \
#     && gulp min

# Entrypoint
# COPY --chown=flask ./docker/flask/entrypoint.sh .
# process the line endings of the shell scripts & convert Windows line endings to UNIX line endings.
RUN sed -i 's/\r$//g' /home/flask/app/docker/flask/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/home/flask/app/docker/flask/entrypoint.sh"]
