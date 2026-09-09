#!/usr/bin/env bash

set -euo pipefail

if [ -z "${TASK_DATABASES:-}" ]; then
  exit 0
fi

IFS=',' read -ra DBS <<< "$TASK_DATABASES"
for db in "${DBS[@]}"; do
  db="$(echo "$db" | xargs)" # обрезать пробелы
  [ -z "$db" ] && continue
  echo "==> создаю базу '$db' (если ещё нет)"
  psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    SELECT 'CREATE DATABASE "$db"'
    WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = '$db')\gexec
EOSQL
done
