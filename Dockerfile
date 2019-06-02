FROM python:3.6-slim

RUN mkdir -p /python-web-server/src
WORKDIR /python-web-server/src

COPY . /python-web-server/src

ENV APP_ENV development

EXPOSE 5035

CMD [ "python", "hello_server.py" ]