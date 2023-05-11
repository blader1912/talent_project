from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


# Lista de rutas de los scripts a ejecutar
def storage():
    import subprocess
    subprocess.call(["python", "C:/Users/bkade/OneDrive/Documentos/scripts/data_storage.py"])


def ingestion():
    import subprocess
    subprocess.call(["python", "C:/Users/bkade/OneDrive/Documentos/scripts/ingestion_data_from_csv.py"])


def transform():
    import subprocess
    subprocess.call(["python", "C:/Users/bkade/OneDrive/Documentos/scripts/transform_data.py"])


# PARAMETROS
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 5, 10),
}

# DAG
dag = DAG('TalentPitch', default_args=default_args, schedule_interval='0 7 * * *')

# TASK
ingest_data = PythonOperator(
    task_id='INGEST_DATA',
    python_callable=ingestion,
    dag=dag
)

tranform_data = PythonOperator(
    task_id='TRANSFORM_DATA',
    python_callable=transform,
    dag=dag
)

storage_data = PythonOperator(
    task_id='STORAGE_DATA',
    python_callable=storage,
    dag=dag
)

# PIPELINE FLOW
ingest_data >> tranform_data >> storage_data
