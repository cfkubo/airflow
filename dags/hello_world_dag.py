from __future__ import annotations

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

# Instantiate a DAG
with DAG(
    dag_id="hello_world_dag",
    schedule=None,
    start_date=pendulum.datetime(2025, 8, 26, tz="UTC"),
    catchup=False,
    tags=["hello_world", "tutorial"],
) as dag:

    # Task 1: Print "Hello, World!"
    task_1 = BashOperator(
        task_id="print_hello_world",
        bash_command="echo 'Hello, World!'",
    )

    # Task 2: Print the current date
    task_2 = BashOperator(
        task_id="print_current_date",
        bash_command="date",
    )

    # Define the task dependency: task_1 must run before task_2
    task_1 >> task_2