1. The "Hello World" Airflow DAG Script
Here is a simple "Hello World" Airflow DAG script. This DAG contains two tasks: one that prints a simple message and another that prints the current date.

Python

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
2. How to Set up a DAG in Airflow
Follow these steps to set up and run your "Hello World" DAG in Airflow.

Step 1: Place the DAG File in the DAGs Folder
Airflow discovers DAGs by looking for Python files in a specific directory. By default, this is the dags/ folder inside your AIRFLOW_HOME directory.

Check your AIRFLOW_HOME directory:

Bash

echo $AIRFLOW_HOME
This will show you the path where Airflow is configured to store its files. It's usually ~/airflow or a path you've explicitly set.

Navigate to the dags/ folder:

Bash

cd $AIRFLOW_HOME/dags
Create the DAG file:
Use a text editor to create a new file named hello_world_dag.py and paste the script from above into it.

Bash

touch hello_world_dag.py

# Open the file in your preferred editor (e.g., nano, vim, VS Code)
# nano hello_world_dag.py


Step 2: Access the Airflow UI
Ensure your Airflow web server and scheduler are running. If you've just started your setup, you can use the airflow standalone command. If you've already configured your airflow.cfg and created a user, you can run the webserver and scheduler separately.

Bash

airflow standalone
or

Bash

airflow webserver --port 8080 &
airflow scheduler &
Open your web browser and go to http://localhost:8080.

Step 3: Trigger the DAG
Locate the DAG:
On the main Airflow UI, you should see a list of all discovered DAGs. Find hello_world_dag in the list.

Unpause the DAG:
The DAG is likely in a "paused" state by default. Look for the toggle button next to the DAG name and switch it to "on." This tells the scheduler to start considering this DAG for execution.

Manually Trigger the DAG:
Click the "Trigger DAG" button (often a play icon) on the right side of the DAG entry. This will immediately create a new DAG run.

Monitor the DAG Run:

Click on the DAG name (hello_world_dag).

This will take you to the DAG's details page. Go to the "Graph View" or "Gantt View" to see the status of the tasks.

As the tasks run, their boxes will change color from grey (scheduled) to green (success).

To see the output of the tasks, click on a task box, then select "Log" from the menu. This will display the standard output, where you can see the "Hello, World!" and the date.

And that's it! You have successfully created, deployed, and run your first Airflow DAG.