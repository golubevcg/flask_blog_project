#!/usr/bin/env bash

echo Run migrations

FLASK_APP=main flask db upgrade

echo migrations ok

echo Init db data

python db_seed_sql_scripts/db_init_seed.py

echo db data ok

exec "$@"
