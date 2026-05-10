from cdl_planejamentocaixa.pipelines.parameters.pipeline_acqua_cotacoes.common import (
    SOURCE_SYSTEM,
    TABLE_SPECS,
)


JDBC_URL = (
    "jdbc:sqlserver://172.19.1.35:1433;"
    "databaseName=BD_THOMPSON;"
    "encrypt=false;trustServerCertificate=true;sslProtocol=TLSv1"
)
JDBC_USER = "airflow"
JDBC_PASSWORD = "A@swy2026"
JDBC_DRIVER = "com.microsoft.sqlserver.jdbc.SQLServerDriver"
READ_OPTIONS = [{"OptionName": "fetchsize", "OptionValue": "10000"}]


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
                        "dbtable": spec["db_object"],
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
