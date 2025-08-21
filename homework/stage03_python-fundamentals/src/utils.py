import pandas as pd

import pandas as pd

def get_summary_stats(df: pd.DataFrame, group_col: str, value_col: str) -> pd.DataFrame:
    if pd.api.types.is_numeric_dtype(df[value_col]):
        agg_spec = {
            "count": "count",
            "mean": "mean",
            "std": "std",
            "min": "min",
            "max": "max",
        }
    else:
        agg_spec = {
            "count": "count",
            "unique_count": pd.Series.nunique
        }

    return (
        df.groupby(group_col, as_index=False)[value_col]
          .agg(**agg_spec)
          .reset_index(drop=True)
    )
