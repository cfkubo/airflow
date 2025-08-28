from __future__ import annotations

import pendulum

from airflow.models.dag import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

with DAG(
    dag_id="postgres_version_check",
    schedule=None,
    start_date=pendulum.datetime(2025, 8, 27, tz="UTC"),
    catchup=False,
    tags=["postgres", "connection_test"],
) as dag:
    # This task uses the SQLExecuteQueryOperator to run a SQL query.
    # It will connect using the 'demo' connection and print the result to logs.
    get_postgres_version = SQLExecuteQueryOperator(
        task_id="get_postgres_version",
        conn_id="demo",
        sql="SELECT version();",
        handler=lambda result: print(f"PostgreSQL Version: {result.fetchone()[0]}"),
    )