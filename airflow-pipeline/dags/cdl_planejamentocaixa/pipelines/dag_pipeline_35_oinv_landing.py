from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

from constructors.pipeline_dag_creator import PipelineDagCreator
from cdl_planejamentocaixa.pipelines.parameters.pipeline_35_oinv.jobs import landing_jobs
from cdl_planejamentocaixa.pipelines.parameters.pipeline_35_oinv.pipeline_landing import pipeline


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}


with DAG(
    "Pipeline_35_OINV_LANDING",
    start_date=datetime(2026, 4, 29),
    max_active_runs=1,
    concurrency=1,
    schedule_interval=None,
    default_args=default_args,
    catchup=False,
) as dag:
    t_start = DummyOperator(task_id="start")
    t_end = DummyOperator(task_id="end")

    pdc = PipelineDagCreator(pipeline, dag)
    for landing_job in landing_jobs:
        pdc.add_job("Landing", landing_job, "PIPELINE_35_OINV")

    pipeline_task_group = pdc.create_pipeline_task_group()
    t_trigger_business = TriggerDagRunOperator(
        task_id="trigger_pipeline_35_oinv_business",
        trigger_dag_id="Pipeline_35_OINV_BUSINESS",
        execution_date="{{ execution_date }}",
    )

    t_start >> pipeline_task_group >> t_trigger_business >> t_end
