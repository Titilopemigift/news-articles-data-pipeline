from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from news_api import run_pipeline

default_args = {
    "owner": "titilope",
    "retries": 1
}

news_dag = DAG(
    dag_id="news_pipeline",
    default_args=default_args,
    description="Fetch news data from API and load into RDS",
    schedule_interval="@daily",
    start_date=datetime(2025, 8, 1),
    catchup=False
)

fetch_and_load_task = PythonOperator(
        task_id="news_articles_to_rds",
        python_callable=run_pipeline,
        dag=news_dag
    )

fetch_and_load_task
