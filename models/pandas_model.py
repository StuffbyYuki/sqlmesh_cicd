import typing as t
from datetime import datetime

import pandas as pd
from sqlmesh import ExecutionContext, model

@model(
    "sqlmesh_example.pandas_example",
    owner="yuki",
    cron="@daily",
    columns={
        "col_a": "int",
        "col_b": "int"
    },
    dialect="duckdb"
)
def execute(
    context: ExecutionContext,
    start: datetime,
    end: datetime,
    execution_time: datetime,
    **kwargs: t.Any,
) -> pd.DataFrame:
    
    return pd.DataFrame({'col_a': [1,2,3], 'col_b': [4,5,6]})

