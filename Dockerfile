FROM python:3.9.6-alpine

WORKDIR /application

COPY src/ .

RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
	; \
	pip install -r requirements.txt; \
	apk del .build-deps;

EXPOSE 5000

#VOLUME /application

CMD uwsgi --http :5000  --manage-script-name --mount /application=app:app --enable-threads --processes 5