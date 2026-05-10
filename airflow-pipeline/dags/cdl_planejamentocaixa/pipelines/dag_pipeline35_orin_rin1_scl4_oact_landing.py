import logging
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.utils.email import send_email

from constructors.pipeline_dag_creator import PipelineDagCreator
from cdl_planejamentocaixa.pipelines.parameters.pipeline_35_orin_rin1_scl4_oact.jobs import (
    landing_jobs,
)
from cdl_planejamentocaixa.pipelines.parameters.pipeline_35_orin_rin1_scl4_oact.pipeline_landing import (
    pipeline,
)


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}


def send_landing_email_best_effort(**context):
    execution_date = context["execution_date"]
    try:
        send_email(
            to=["luiz.antonio@ambipar.com"],
            subject="Pipeline35_ORIN_RIN1_SCL4_OACT_Landing finalizado",
            html_content=f"""
            <p>As tabelas ORIN, RIN1, SCL4 e OACT do servidor 172.19.1.35 foram copiadas para a Landing.</p>
            <p>Pipeline: Pipeline35_ORIN_RIN1_SCL4_OACT_Landing</p>
            <p>Execucao: {execution_date}</p>
            """,
        )
    except Exception:
        logging.exception(
            "Falha ao enviar e-mail da Pipeline35_ORIN_RIN1_SCL4_OACT_Landing. O fluxo seguira normalmente."
        )


with DAG(
    "Pipeline35_ORIN_RIN1_SCL4_OACT_Landing",
    start_date=datetime(2026, 4, 30),
    max_active_runs=1,
    concurrency=4,
    schedule_interval=None,
    default_args=default_args,
    catchup=False,
) as dag:
    t_start = DummyOperator(task_id="start")
    t_end = DummyOperator(task_id="end")

    pdc = PipelineDagCreator(pipeline, dag)
    for landing_job in landing_jobs:
        pdc.add_job("Landing", landing_job, "PIPELINE_35_ORIN_RIN1_SCL4_OACT")

    pipeline_task_group = pdc.create_pipeline_task_group()

    t_email = PythonOperator(
        task_id="send_landing_email",
        python_callable=send_landing_email_best_effort,
        provide_context=True,
    )

    t_start >> pipeline_task_group >> t_email >> t_end
