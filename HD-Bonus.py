#!/usr/bin/env python
# coding: utf-8

# # Bonus - Create a DAG to schedule the process using Airflow.

# In[10]:


# !pip install apache-airflow
# !airflow db init


# In[1]:


import datetime

from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.python import PythonSensor


# Define functions
def job_1():
    print("Perform job 1")


def job_2():
    print("Perform job 2")


def sensor_job():
    print("Sensor Job")


# In[2]:


# Parameters
WORFKLOW_DAG_ID = "my_example_dag"
WORFKFLOW_START_DATE = datetime.datetime(2022, 1, 1)
WORKFLOW_SCHEDULE_INTERVAL = "* * * * *"
WORKFLOW_EMAIL = ["youremail@example.com"]

WORKFLOW_DEFAULT_ARGS = {
    "owner": "kiran",
    "start_date": WORFKFLOW_START_DATE,
    "email": WORKFLOW_EMAIL,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
}


# In[3]:


# Initialize DAG
dag = DAG(
    dag_id=WORFKLOW_DAG_ID,
    schedule_interval=WORKFLOW_SCHEDULE_INTERVAL,
    default_args=WORKFLOW_DEFAULT_ARGS,
)

# Define jobs
job_1_operator = PythonOperator(
    task_id="task_job_1",
    python_callable=job_1,
    dag=dag,
)

job_2_sensor = PythonSensor(
    task_id="task_job_2_sensor",
    python_callable=sensor_job,
    dag=dag,
    poke_interval=180,
)

job_2_operator = PythonOperator(
    task_id="task_job_2",
    python_callable=job_2,
    dag=dag,
)


# In[4]:


# Set dependency
job_1_operator >> job_2_sensor >> job_2_operator


# ## We can copy the file path or change the DAGs folder
# $ cp dags_folder/dag.py/home/USER/airflow/dags/

# In[ ]:


# Then launch the web server with credentials 


# In[1]:


# Launch the scheduler

