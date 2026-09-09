include .env

.PHONY: up down apply clone reset

up:
	docker compose up -d
	docker compose exec postgres sh -c "until pg_isready -U $(POSTGRES_USER) -d $(POSTGRES_DB); do sleep 1; done"

down:
	docker compose down

apply:
	for f in $(TASK)/*.sql; do echo "==> [$(TASK)] $$f"; docker compose exec -T postgres psql -U $(POSTGRES_USER) -d $(TASK) -v ON_ERROR_STOP=1 -f - < $$f; done

clone:
	docker compose exec -T postgres sh -c "pg_dump -U $(POSTGRES_USER) --clean --if-exists -d $(FROM) | psql -U $(POSTGRES_USER) -d $(TO) -v ON_ERROR_STOP=1"

reset:
	docker compose exec -T postgres psql -U $(POSTGRES_USER) -d $(POSTGRES_DB) -v ON_ERROR_STOP=1 -c "DROP DATABASE IF EXISTS \"$(TASK)\";" -c "CREATE DATABASE \"$(TASK)\";"
