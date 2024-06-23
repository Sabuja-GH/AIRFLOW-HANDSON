from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow import DAG 


# Define default arguments for the DAG
default_args = {
    'owner': 'Vinoo',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'catchup': False,
    'start_date': datetime(2023, 1, 1)
}
# Define the DAG object
dag = DAG(
    dag_id='one_task_dag', 
    default_args=default_args,
    description='A simple DAG to write text to a file using BashOperator',
    schedule_interval=None,
)
# bash operatoe (used to run the commands to createthe file)

task1 = BashOperator(
        task_id='one_task', 
        bash_command='echo "Hello, LinkedIn Learning!" > /workspaces/AIRFLOW-HANDSON/airflow/lab/files/one_task_dag.txt',
        dag=dag
    )

