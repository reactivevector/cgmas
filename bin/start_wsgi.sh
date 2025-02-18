#!/bin/bash

APP_ENV="${APP_ENV:-dev}"

if [ "$APP_ENV" = "dev" ]; then
    uv run flask --app cgmas.app:APP run --debug --host=0.0.0.0 --port=5050
elif [ "$APP_ENV" = "prod" ]; then
    uv run waitress-serve --host=0.0.0.0 --port=5050 cgmas.app:APP
else
    echo "Error: Invalid APP_ENV value. Must be 'dev' or 'prod'"
    exit 1
fi