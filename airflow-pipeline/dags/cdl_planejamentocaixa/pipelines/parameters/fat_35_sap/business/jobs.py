fat_sap_oinv_rin1_orin = {
    "DatasetName": "fat_sap_oinv_rin1_orin",
    "SourceSystem": "faturamento_sap",
    "NumOfDpus": 4,
    "Stages": [
        {
            "ExternalFunction": {
                "Module": "pyspark_library.planejamento_caixa.transformations.business.sap_fat_oinv_rin1_orin",
                "Parameters": [],
            },
            "Input": [
                {
                    "InputAlias": "sap_oinv",
                    "Delete": False,
                    "ReadFormat": "parquet",
                    "RepartitionValue": 20,
                    "DatasetName": "OINV_Integration",
                },
                {
                    "InputAlias": "sap_rin1",
                    "Delete": False,
                    "ReadFormat": "parquet",
                    "RepartitionValue": 20,
                    "DatasetName": "RIN1_Integration",
                },
                {
                    "InputAlias": "sap_orin",
                    "Delete": False,
                    "ReadFormat": "parquet",
                    "RepartitionValue": 20,
                    "DatasetName": "ORIN_Integration",
                },
            ],
            "Output": {
                "MergeType": "Replace/ExecutionDatetime",
                "Coalesce": 1,
                "OutputPath": "s3a://business/faturamento_sap/fat_sap_oinv_rin1_orin",
            },
        }
    ],
}
