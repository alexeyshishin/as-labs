# БД — лабы, семестр 5

Postgres в docker-compose, у каждого задания своя база (`task1` … `task7`).

## Команды

```bash
make up                              # поднять postgres, создать базы
make apply TASK=task1                # накатить *.sql из папки в её базу
make clone FROM=task1 TO=task2       # склонировать текущее состояние базы task1 в task2
make reset TASK=task2                # дропнуть и пересоздать пустую базу
make down                            # остановить контейнер
```

## Структура

`taskN/` — независимое задание, база `taskN`:
- `taskN.md` — условие
- `01_schema.sql`, `02_data.sql`, `03_queries.sql` — накатываются по порядку через `apply`

Если задание продолжает предыдущее — сначала `make clone FROM=... TO=...`, потом добавляй в `taskN/` новые `*.sql` поверх склонированного состояния.

## Переменные окружения
``` 
POSTGRES_PASSWORD=SUPER_PASS
POSTGRES_USER=SUPER_USER
POSTGRES_DB=SUPER_DB
POSTGRES_PORT=5432

TASK_DATABASES=task1,task2,task3,task4,task5,task6,task7
DATABASE_URL=postgresql://SUPER_USER:SUPER_PASS@localhost:5432/SUPER_DB
```