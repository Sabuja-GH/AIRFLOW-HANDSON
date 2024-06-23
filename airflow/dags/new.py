from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow import DAG

default_args = {
    'owner': 'Vinoo',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'catchup': False,
    'start_date': datetime(2023, 1, 1)
}

with DAG(
    dag_id='newdag',
    description='A DAG with two tasks',
    schedule_interval=None,
    default_args=default_args
) as dag:

    task1 = BashOperator(
        task_id='task1',
        bash_command='echo "Task 1: sleeping" ; sleep 5 ; echo "hello"',
        dag=dag
    )

    task2 = BashOperator(
        task_id='task2',
        bash_command='echo "Task 2: hello world"',
        dag=dag
    )

    task1 >> task2 