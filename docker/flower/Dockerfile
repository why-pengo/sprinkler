FROM python:3.7.2-alpine3.8

LABEL maintainer="Jon.Morgan@FirstData.com"
LABEL version="1.0"

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  PIPENV_HIDE_EMOJIS=true \
  PIPENV_COLORBLIND=true \
  PIPENV_NOSPIN=true \
  BROKER=${BROKER:-'amqp://guest:guest@localhost/%2F'}

RUN apk --no-cache add \
    bash \
    build-base \
    curl \
    gcc \
    gettext \
    libffi-dev \
    linux-headers \
    musl-dev \
    openldap-dev \
    tini
#    openssl-dev \ it's libressl-dev on Apline, but it get picked up

# Creating folders, and files for a project:
COPY . /app
WORKDIR /app

# Project initialization:
RUN pip install pipenv && pipenv install --deploy --system

# celery flower -A tasks --loglevel=info
# this is the preference form, but does not do variable expansion
# CMD ["celery", "flower", "-A", "tasks", "--broker=amqp://guest:guest@localhost//", "--loglevel=info"]
# this is the shell form that does variable expansion
CMD /usr/local/bin/celery flower -A tasks --broker=${BROKER} --loglevel=info
