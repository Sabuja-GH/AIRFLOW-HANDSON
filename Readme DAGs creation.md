# Location where airflows expect DAGS to be 
cat airflow/airflow.cfg | grep dags_folder (**grep is used to look for dag_folder**)

from datetime import datetime(**used to specify a start date**)
from airflow.operators.bash import BashOperator (**since we're using a bash command, we'll also import the bash operator. Operators are libraries that facilitate the interface with external tools and systems.**)
from airflow import DAG (**All DAGs then require importing the DAG class from the Airflow package**)


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
    dag_id='one_task_dag', (**name of the dag**)
    default_args=default_args,
    description='A simple DAG to write text to a file using BashOperator',
    schedule_interval=None,(**freq at which the dag should run**)
)
# bash operatoe (used to run the commands to createthe file)

task1 = BashOperator(
        task_id='one_task', (**name of the task within the dag**)
        bash_command='echo "Hello, LinkedIn Learning!" > /workspaces/AIRFLOW-HANDSON/airflow/lab/files/one_task_dag.txt', ( **actual bash commnand, In this case the bash command will echo Hello LinkedIn Learning to a file called one_task_dag.txt.**)
        dag=dag
    )

**Then run validate the sntac of the file bu runnog the regular python cmd against the file in terminal.**

    python -W ignore /workspaces/AIRFLOW-HANDSON/airflow/dags/one_task_dag.py (-W inores the warnings)

sometimes dag wont show because of scheduler issue, then use code " $ airflow scheduler" (Start the scheduler without daemon mode). Then run other cmds in differnet termial. to close the scheduler use ctrl+c. 

**Now dag will be shown in webserver, friom there run it there.once dag run co,pleted successfully we can check i fthe text file has been generated or not.**

    cat /workspaces/AIRFLOW-HANDSON/airflow/lab/files/one_task_dag.txt

    TWO task dag++

    bash_command='echo "sleeping...." ; sleep 5; echo "second task complete!"' , - outputs txt 'sleeping..', then sleeps for 5 sec, then outputs 'second task complete!'
    task1 >> task2 - task 2 is made dependant on task 1 i.e, once task 1 is completed only then task 2 willl run