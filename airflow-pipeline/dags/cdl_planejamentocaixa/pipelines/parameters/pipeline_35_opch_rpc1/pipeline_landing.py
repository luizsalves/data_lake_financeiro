pipeline = {
    "PipelineName": "Pipeline_35_OPCH_RPC1_LANDING",
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
