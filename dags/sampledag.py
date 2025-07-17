from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

def hello_airflow():
    logger.info("Hello from Airflow!")

def print_datetime_from_sql(ti):
    result = ti.xcom_pull(task_ids='select_datetime')
    # SQLExecuteQueryOperator returns a list of tuples
    if result and len(result) > 0:
        logger.info(f"Datetime from SQL: {result[0][0]}")
    else:
        logger.warning("No datetime returned from SQL.")

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

    select_datetime_task = SQLExecuteQueryOperator(
        task_id='select_datetime',
        conn_id='postgres_default',
        sql="SELECT NOW();"
    )

    print_datetime_task = PythonOperator(
        task_id='print_datetime',
        python_callable=print_datetime_from_sql,
    )

    hello_task >> select_datetime_task >> print_datetime_task
