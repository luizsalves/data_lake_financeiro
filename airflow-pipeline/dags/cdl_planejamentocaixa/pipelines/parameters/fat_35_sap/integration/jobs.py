sap_oinv = {
    "DatasetName": "OINV_Integration",
    "SourceSystem": "pipeline_35_oinv",
    "NumOfDpus": 4,
    "Stages": [
        {
            "ExternalFunction": {
                "Module": "pyspark_library.planejamento_caixa.transformations.raw_integration.SAP_OINV",
                "Parameters": [],
            },
            "Input": [
                {
                    "InputAlias": "df_sap_oinv",
                    "Delete": False,
                    "ReadFormat": "parquet",
                    "RepartitionValue": 20,
                    "InputType": "Full",
                    "InputPath": "s3a://landing/pipeline_35_oinv/OINV_Landing",
                }
            ],
            "Output": {
                "MergeType": "Replace/ExecutionDatetime",
                "Coalesce": 1,
                "DisableCatalog": True,
                "OutputPath": "s3a://integration/pipeline_35_oinv/OINV_Integration",
            },
        }
    ],
}


sap_rin1 = {
    "DatasetName": "RIN1_Integration",
    "SourceSystem": "pipeline_35_orin_rin1_scl4_oact",
    "NumOfDpus": 4,
    "Stages": [
        {
            "ExternalFunction": {
                "Module": "pyspark_library.planejamento_caixa.transformations.raw_integration.SAP_RIN1",
                "Parameters": [],
            },
            "Input": [
                {
                    "InputAlias": "df_sap_rin1",
                    "Delete": False,
                    "ReadFormat": "parquet",
                    "RepartitionValue": 20,
                    "InputType": "Full",
                    "InputPath": "s3a://landing/pipeline_35_orin_rin1_scl4_oact/RIN1_Landing",
                }
            ],
            "Output": {
                "MergeType": "Replace/ExecutionDatetime",
                "Coalesce": 1,
                "DisableCatalog": True,
                "OutputPath": "s3a://integration/pipeline_35_orin_rin1_scl4_oact/RIN1_Integration",
            },
        }
    ],
}


sap_orin = {
    "DatasetName": "ORIN_Integration",
    "SourceSystem": "pipeline_35_orin_rin1_scl4_oact",
    "NumOfDpus": 4,
    "Stages": [
        {
            "ExternalFunction": {
                "Module": "pyspark_library.planejamento_caixa.transformations.raw_integration.SAP_ORIN",
                "Parameters": [],
            },
            "Input": [
                {
                    "InputAlias": "df_sap_orin",
                    "Delete": False,
                    "ReadFormat": "parquet",
                    "RepartitionValue": 20,
                    "InputType": "Full",
                    "InputPath": "s3a://landing/pipeline_35_orin_rin1_scl4_oact/ORIN_Landing",
                }
            ],
            "Output": {
                "MergeType": "Replace/ExecutionDatetime",
                "Coalesce": 1,
                "DisableCatalog": True,
                "OutputPath": "s3a://integration/pipeline_35_orin_rin1_scl4_oact/ORIN_Integration",
            },
        }
    ],
}
