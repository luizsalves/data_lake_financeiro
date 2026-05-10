#!/bin/bash

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && cd .. && pwd)"

cd $PROJECT_DIR

docker-compose down
docker-compose rm
docker volume rm airflow-datapipeline_postgres-db-volume
docker volume rm airflow-pipeline_postgres-db-volume

sudo rm -rf logs