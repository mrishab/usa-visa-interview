.PHONY: build

APP_NAME:=usa-visa-appointment
VERSION:=1.0.0-SNAPSHOT

dev:
	docker-compose -f docker-compose.yml -f docker-compose-run.yml -f docker-compose-dev.yml run --rm app

build:
	docker build . -t ${APP_NAME}:${VERSION}

run:
	docker-compose -f docker-compose.yml -f docker-compose-run.yml down &&\
	docker-compose -f docker-compose.yml -f docker-compose-run.yml rm &&\
	docker-compose -f docker-compose.yml -f docker-compose-run.yml build --no-cache &&\
	docker-compose -f docker-compose.yml -f docker-compose-run.yml up
