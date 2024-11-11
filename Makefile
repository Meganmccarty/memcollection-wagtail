.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# Docker commands
build: ## Builds Docker containers for the Wagtail app and Postgres database
	docker compose build

build-no-cache: ## Builds Docker containers without caching
	docker compose build --no-cache

up: ## Builds and runs Docker containers for the Wagtail app and database
	docker compose up

down: ## Tears down the Docker containers
	docker compose down

prune: ## Prunes Docker system, containers, mages, and volumes
	docker system prune; docker container prune; docker image prune; docker volume prune

# Docker commands for M chip Macs
mac-build: ## Builds Docker containers for the Wagtail app and Postgres database for M chip Macs
	docker compose -f docker-compose.yaml -f docker-compose.mac-m.yaml build

mac-build-no-cache: ## Builds Docker containers without caching for M chip Macs
	docker compose -f docker-compose.yaml -f docker-compose.mac-m.yaml build --no-cache

mac-up: ## Builds and runs Docker containers for the Wagtail app and database for M chip Macs
	docker compose -f docker-compose.yaml -f docker-compose.mac-m.yaml up

# Wagtail commands
makemigrations: ## Makes migrations of the Wagtail app within the Docker container
	docker compose run --rm web python manage.py makemigrations

migrate: ## Migrates the database of the Wagtail app within the Docker container
	docker compose run --rm web python manage.py migrate

createsuperuser: ## Creates a super user for the Wagtail app
	docker compose run --rm web python manage.py createsuperuser

create-app: ## Creates new Django app (must set 'name=YOUR-APP-NAME')
	docker compose run --rm web python manage.py startapp $(name)

# Linting and formatting commands
lint: ## Lints Python code using flake8
	docker compose run --rm web python -m flake8 .

format: ## Formats Python code using Black formatter
	docker compose run --rm web python -m black .

# Deploy commands
fly-auth: ## Authenticates to Fly.io
	fly auth login

fly-secrets: ## Sets up Fly.io to use the .env.production secrets file
	flyctl secrets import < .env.production

fly-deploy: ## Deploys to Fly.io
	make fly-secrets && \
	fly deploy --ha=false