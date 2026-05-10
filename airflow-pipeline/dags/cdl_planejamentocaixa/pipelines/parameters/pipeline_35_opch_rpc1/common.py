SOURCE_SYSTEM = "pipeline_35_opch_rpc1"


TABLE_NAMES = [
    "OPCH",
    "RPC1",
]


TABLE_SPECS = [
    {
        "table_name": table_name,
        "db_object": f"dbo.{table_name}",
        "landing_dataset": f"{table_name}_Landing",
        "integration_dataset": f"{table_name}_Integration",
        "business_dataset": f"{table_name}_Business",
    }
    for table_name in TABLE_NAMES
]
