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
    dag_id='Two_task_dag', 
    default_args=default_args,
    description='A simple DAG to execute 2 tasks',
    schedule_interval=None,
)
# bash operatoe (used to run the commands to createthe file)

task1 = BashOperator(
        task_id='one_task', 
        bash_command='echo "first task complete!" ' ,
        dag=dag
    )

# in the bash command, first we echo txt > sleep for 5 sec > againn
task2 = BashOperator(
        task_id='Two_task', 
        bash_command='echo "sleeping...." ; sleep 5; echo "second task complete!"' ,
        dag=dag
    )

# Set task dependencies
task1 >> task2
