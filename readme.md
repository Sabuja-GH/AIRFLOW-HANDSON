# Download airflow (
   /workspaces/AIRFLOW-HANDSON/airflow- location where airflow will be installed.

    change the airflow version to latest one here it is 2.9.2 and give the python version that is present in the system, here it is 3.10.13)

export AIRFLOW_HOME="/workspaces/AIRFLOW-HANDSON/airflow" &&
pip install "apache-airflow==2.9.2" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.2/constraints-3.10.txt"

# prints full set of functions available
airflow

# instialize airflow DB
airflow db init

# Run Airflow Info
airflow info
# create user "admin" with password "password"
airflow users create --username admin --firstname Firstname --lastname Lastname --role Admin --email admin@example.org --password password

# Run airflow webserver
airflow webserver -D

-D is used to run the code as a background process.

WTF_CSRF_ENABLED = False, make this change in webserver_config.py so no error won't pop. After ddoing this kill the webserver and then again run it. so no error wont come.

# prints all the existing dags
(shows all the existing dags in airflow webserver)
airflow dags list

# Run airflow scheduler 
airflow scheduler -D

{{{
# Delete a user in aiflow (admin is being deleted)
airflow users delete -u admin
# users list
airflow users list}}}}



# STOP webserver
cat $AIRFLOW_HOME/airflow-webserver.pid | xargs kill
echo ""> $AIRFLOW_HOME/airflow-webserver.pid

OR

(look for the pid of webserver using folowing cmd and then kill it, same withscheduler but code is lil differnet)

ps -ef | grep -i webserver | grep master
kill {pid}

{{{
To kill them best practice is to first kill pid(process id) then overwrite the pisd file with empty string.

cat - is used to open a file from directory

xarg- is used to pass multiple pids so they can be killed using kill argumnet

echo''- it is used to pass an empty string to the pid doc.
}}}

# Stop scheduler
cat $AIRFLOW_HOME/airflow-scheduler.pid | xargs kill
echo ""> $AIRFLOW_HOME/airflow-scheduler.pid

OR 
ps -ef | grep -i scheduler | grep -v grep | grep -v DagFileProcessorManager
kill {pid}