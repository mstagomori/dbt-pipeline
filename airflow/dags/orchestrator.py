import sys
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta

sys.path.append('/opt/airflow/api-request')
def safe_main_callable():
    from insert_data import run
    return run()

default_args = {
    'description': 'Orchestrator DAG',
    'start_date': datetime(2026,2,5),
    'catchup': False,
}

dag = DAG(
    dag_id='financial-data-orchestrator',
    default_args=default_args,
    schedule=timedelta(minutes=1)
)

with dag:
    task1 = PythonOperator(
        task_id='ingest_data',
        python_callable=safe_main_callable
    )