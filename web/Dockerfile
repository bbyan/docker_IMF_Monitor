FROM python:2.7
ENV PYTHONUNBUFFERED 1

ENV APP_USER myapp
ENV APP_ROOT /app

WORKDIR /app
RUN groupadd -r ${APP_USER} \
    && useradd -r -m \
    --home-dir ${APP_ROOT} \
    -s /usr/sbin/nologin \
    -g ${APP_USER} ${APP_USER}

COPY ./requirements.txt /app/config/requirements.txt
RUN pip install -r /app/config/requirements.txt
USER ${APP_USER}
COPY . /app


