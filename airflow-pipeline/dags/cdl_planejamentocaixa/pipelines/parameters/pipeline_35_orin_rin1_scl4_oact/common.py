SOURCE_SYSTEM = "pipeline_35_orin_rin1_scl4_oact"


TABLE_SPECS = [
    {
        "table_name": "ORIN",
        "landing_dataset": "ORIN_Landing",
        "sql_query": """
            SELECT
                R0.COD_FILIAL,
                R0.DocEntry,
                R0.DocNum,
                R0.DocType,
                R0.CANCELED,
                R0.DocStatus,
                R0.InvntSttus,
                R0.Transfered,
                R0.ObjType,
                R0.DocDate,
                R0.DocDueDate,
                R0.CardCode,
                R0.CardName,
                R0.Address,
                R0.DocCur,
                R0.DocRate,
                R0.DocTotal,
                R0.DocTotalFC,
                R0.PaidToDate,
                R0.PaidFC,
                R0.Comments,
                R0.JrnlMemo,
                R0.TransId,
                R0.ReceiptNum,
                R0.GroupNum,
                R0.DocTime
            FROM temp_BD_INADIMPLENCIA.dbo.ORIN R0
        """.strip(),
    },
    {
        "table_name": "RIN1",
        "landing_dataset": "RIN1_Landing",
        "sql_query": """
            SELECT
                R1.COD_FILIAL,
                R1.DocEntry,
                R1.BaseEntry,
                R1.BaseType
            FROM temp_BD_INADIMPLENCIA.dbo.RIN1 R1
        """.strip(),
    },
    {
        "table_name": "SCL4",
        "landing_dataset": "SCL4_Landing",
        "sql_query": """
            SELECT
                L4.SrcvCallID,
                L4.Object,
                L4.DocNumber,
                L4.COD_FILIAL
            FROM temp_BD_INADIMPLENCIA.dbo.SCL4 L4
        """.strip(),
    },
    {
        "table_name": "OACT",
        "landing_dataset": "OACT_Landing",
        "sql_query": """
            SELECT
                *
            FROM temp_BD_INADIMPLENCIA.dbo.OACT
        """.strip(),
    },
]
