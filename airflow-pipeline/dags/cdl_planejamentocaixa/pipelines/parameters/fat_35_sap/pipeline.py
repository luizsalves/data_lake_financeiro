pipeline = {
    "PipelineName": "Pipeline_35_Faturamento_SAP_v1",
    "Flows": [
        {
            "FlowName": "Landing",
            "Stages": [
                {
                    "StageName": "Reference",
                    "ComputeProfile": "landing2raw",
                    "ExecutionPartitionLabel": "execution_ts",
                    "Output": {
                        "StorageLayer": "landing",
                        "MergeType": "Replace/ExecutionDatetime",
                        "Coalesce": 1,
                    },
                }
            ],
        },
        {
            "FlowName": "Integration",
            "Stages": [
                {
                    "StageName": "Upsert",
                    "ExecutionPartitionLabel": "execution_ts",
                    "ComputeProfile": "raw2integration",
                    "Input": {
                        "ReadFormat": "parquet",
                        "InputType": "Full",
                    },
                    "Output": {
                        "StorageLayer": "integration",
                        "MergeType": "Replace/ExecutionDatetime",
                        "Coalesce": 1,
                    },
                }
            ],
        },
        {
            "FlowName": "Business",
            "Stages": [
                {
                    "StageName": "Transform",
                    "ComputeProfile": "integration2business",
                    "ExecutionPartitionLabel": "execution_ts",
                    "Input": {
                        "InputType": "Full",
                    },
                    "Output": {
                        "StorageLayer": "business",
                        "MergeType": "Replace/ExecutionDatetime",
                        "Coalesce": 1,
                    },
                }
            ],
        },
    ],
}
