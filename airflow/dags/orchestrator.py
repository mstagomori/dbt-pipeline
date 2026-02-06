import sys
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount

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
    dag_id='financial-api-dbt-orchestrator',
    default_args=default_args,
    schedule=timedelta(minutes=1)
)

with dag:
    task1 = PythonOperator(
        task_id='ingest_data',
        python_callable=safe_main_callable
    )

    task2 = DockerOperator(
        task_id='transform_data',
        image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command='run',
        working_dir= '/usr/app',
        mounts=[
            Mount(source='/mnt/d/Arquivos/Trabalho/Projetos/dbt-pipeline/dbt/my_project', 
                  target='/usr/app', 
                  type='bind'),
            Mount(source='/mnt/d/Arquivos/Trabalho/Projetos/dbt-pipeline/dbt/profiles.yml', 
                  target='/root/.dbt/profiles.yml', 
                  type='bind')
        ],
        network_mode='dbt-pipeline_my-network',
        docker_url='unix://var/run/docker.sock',
        auto_remove='success'
    )

    task1 >> task2