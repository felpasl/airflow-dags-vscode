from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def hello_airflow():
    print("Hello from Airflow!")

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='sample_hello_dag',
    default_args=default_args,
    description='A simple sample DAG',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['example'],
) as dag:
    hello_task = PythonOperator(
        task_id='say_hello',
        python_callable=hello_airflow,
    )
