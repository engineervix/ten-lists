FROM python:3.8-slim-bullseye

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
    FLASK_ENV=production \
    # NODE_ENV=production \
    USER=flask \
    PATH=/home/flask/app/node_modules/.bin:$PATH

# Install system dependencies
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    curl \
    ffmpeg \
    git \
    libjpeg62-turbo-dev \
    libmariadb-dev-compat libmariadb-dev \
    libpq-dev \
    libwebp-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# install Node.js
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt install nodejs -y
RUN npm install -g grunt-cli

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

# Copy the source code of the project into the container
COPY --chown=flask:flask . .

# Generate static assets
RUN npm run build

# Runtime command that executes when "docker run" is called
CMD ["gunicorn", "tenlists.webapp.ten_lists:create_app()"]
