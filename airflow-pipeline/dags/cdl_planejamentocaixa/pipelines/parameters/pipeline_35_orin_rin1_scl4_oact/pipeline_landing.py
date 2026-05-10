pipeline = {
    "PipelineName": "Pipeline35_ORIN_RIN1_SCL4_OACT_Landing",
    "Flows": [
        {
            "FlowName": "Landing",
            "Stages": [
                {
                    "StageName": "Extract",
                    "ComputeProfile": "jdbc2landing",
                    "ExecutionPartitionLabel": "execution_ts",
                    "Output": {
                        "StorageLayer": "landing",
                        "MergeType": "Replace/ExecutionDatetime",
                        "PersistExecutionPartitionColumn": True,
                        "Coalesce": 1,
                    },
                }
            ],
        }
    ],
}
