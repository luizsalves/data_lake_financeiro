from cdl_planejamentocaixa.pipelines.parameters.pipeline_35_orin_rin1_scl4_oact.common import (
    SOURCE_SYSTEM,
    TABLE_SPECS,
)


JDBC_URL = (
    "jdbc:sqlserver://172.19.1.35:1433;"
    "databaseName=temp_BD_INADIMPLENCIA;"
    "encrypt=false;trustServerCertificate=true;sslProtocol=TLSv1"
)
JDBC_USER = "airflow"
JDBC_PASSWORD = "A@swy2026"
JDBC_DRIVER = "com.microsoft.sqlserver.jdbc.SQLServerDriver"
READ_OPTIONS = [{"OptionName": "fetchsize", "OptionValue": "10000"}]


def _dbtable_for_spec(spec):
    if "sql_query" in spec:
        return f"({spec['sql_query']}) AS src"
    return spec["db_object"]


landing_jobs = [
    {
        "DatasetName": spec["landing_dataset"],
        "SourceSystem": SOURCE_SYSTEM,
        "Stages": [
            {
                "Input": [
                    {
                        "InputType": "Full",
                        "InputAlias": "df_input",
                        "ReadFormat": "jdbc",
                        "url": JDBC_URL,
                        "user": JDBC_USER,
                        "password": JDBC_PASSWORD,
                        "driver": JDBC_DRIVER,
                        "dbtable": _dbtable_for_spec(spec),
                        "ReadOptions": READ_OPTIONS,
                    }
                ],
                "ExternalFunction": {
                    "Module": "pyspark_library.dummy",
                    "Parameters": [],
                },
                "Output": {
                    "Coalesce": 1,
                },
            }
        ],
    }
    for spec in TABLE_SPECS
]
