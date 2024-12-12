import typing as t
from datetime import datetime

import pandas as pd
import polars as pl
from sqlmesh import ExecutionContext, model

@model(
    "sqlmesh_example.polars_example",
    owner="yuki",
    cron="@daily",
    columns={
        "col_a": "int",
        "col_b": "int",
        "col_c": "boolean",
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
    
    df = pl.DataFrame({'col_a': [1,2,3], 'col_b': [4,5,6]})

    return (
        df
        .with_columns(
            col_c=pl.col('col_a').eq(1)
        )
        .to_pandas()
    )
