from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.utils.email import send_email
from datetime import datetime, timedelta
import logging

from constructors.pipeline_dag_creator import PipelineDagCreator
from cdl_planejamentocaixa.pipelines.parameters.fat_35_sap.integration.jobs import *
from cdl_planejamentocaixa.pipelines.parameters.fat_35_sap.pipeline import pipeline
from cdl_planejamentocaixa.pipelines.parameters.fat_35_sap.business.jobs import *
from cdl_planejamentocaixa.pipelines.parameters.pipeline_35_oinv.jobs import landing_jobs as landing_jobs_oinv
from cdl_planejamentocaixa.pipelines.parameters.pipeline_35_oinv.pipeline_landing import pipeline as pipeline_35_oinv_landing
from cdl_planejamentocaixa.pipelines.parameters.pipeline_35_orin_rin1_scl4_oact.jobs import landing_jobs as landing_jobs_orin_rin1
from cdl_planejamentocaixa.pipelines.parameters.pipeline_35_orin_rin1_scl4_oact.pipeline_landing import pipeline as pipeline_35_orin_rin1_landing


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}


def send_pipeline_email_best_effort(**context):
    execution_date = context["execution_date"]
    try:
        send_email(
            to=["luiz.antonio@ambipar.com"],
            subject="Pipeline_35_Faturamento_SAP_v1 finalizado",
            html_content=f"""
            <p>A pipeline Pipeline_35_Faturamento_SAP_v1 foi finalizada com sucesso.</p>
            <p>Foram processadas as tabelas OINV, RIN1 e ORIN das camadas Landing, Integration e Business.</p>
            <p>Pipeline: Pipeline_35_Faturamento_SAP_v1</p>
            <p>Execucao: {execution_date}</p>
            """,
        )
    except Exception:
        logging.exception(
            "Falha ao enviar e-mail da Pipeline_35_Faturamento_SAP_v1. O fluxo seguira normalmente."
        )


with DAG(
    "Pipeline_35_Faturamento_SAP_v1",
    start_date=datetime(2026, 5, 3),
    max_active_runs=3,
    schedule_interval=None,
    default_args=default_args,
    catchup=False,
) as dag:

    t_start = DummyOperator(task_id="start")
    t_end = DummyOperator(task_id="end")

    pdc = PipelineDagCreator(pipeline, dag)

    # Landing (referencia externa)
    for landing_job in landing_jobs_oinv:
        if landing_job["DatasetName"] == "OINV_Landing":
            pdc.add_job_external(pipeline_35_oinv_landing, "Landing", landing_job, "FaturamentoSAP")

    for landing_job in landing_jobs_orin_rin1:
        if landing_job["DatasetName"] in ("ORIN_Landing", "RIN1_Landing"):
            pdc.add_job_external(pipeline_35_orin_rin1_landing, "Landing", landing_job, "FaturamentoSAP")

    # Integration
    pdc.add_job("Integration", sap_oinv, "FaturamentoSAP")
    pdc.add_job("Integration", sap_rin1, "FaturamentoSAP")
    pdc.add_job("Integration", sap_orin, "FaturamentoSAP")

    # Business
    pdc.add_job("Business", fat_sap_oinv_rin1_orin, "FaturamentoSAP")

    pipeline_task_group = pdc.create_pipeline_task_group()

    landing_oinv = dag.get_task(
        "Pipeline_35_Faturamento_SAP_v1.Landing.Reference.FaturamentoSAP.External_OINV_Landing"
    )
    landing_rin1 = dag.get_task(
        "Pipeline_35_Faturamento_SAP_v1.Landing.Reference.FaturamentoSAP.External_RIN1_Landing"
    )
    landing_orin = dag.get_task(
        "Pipeline_35_Faturamento_SAP_v1.Landing.Reference.FaturamentoSAP.External_ORIN_Landing"
    )

    integration_oinv = dag.get_task(
        "Pipeline_35_Faturamento_SAP_v1.Integration.Upsert.FaturamentoSAP.OINV_Integration"
    )
    integration_rin1 = dag.get_task(
        "Pipeline_35_Faturamento_SAP_v1.Integration.Upsert.FaturamentoSAP.RIN1_Integration"
    )
    integration_orin = dag.get_task(
        "Pipeline_35_Faturamento_SAP_v1.Integration.Upsert.FaturamentoSAP.ORIN_Integration"
    )

    landing_oinv >> integration_oinv
    landing_rin1 >> integration_rin1
    landing_orin >> integration_orin

    integration_oinv >> integration_rin1 >> integration_orin

    t_email = PythonOperator(
        task_id="send_pipeline_email",
        python_callable=send_pipeline_email_best_effort,
        provide_context=True,
    )

    t_start >> pipeline_task_group >> t_email >> t_end
