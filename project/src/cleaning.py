import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def fill_missing(
    df: pd.DataFrame,
    columns=None,
    method: str = "median",
    allow_bfill: bool = True,
) -> pd.DataFrame:
    """
    Fill missing values.
    - method='ffill' -> forward-fill (recommended for monthly macro series)
    - method='median' -> per-column median (useful for cross-sectional features)
    - method='none' -> no filling (return copy)
    If ffill leaves leading NaNs, optionally backfill the first gap (allow_bfill).
    """
    out = df.copy()
    if columns is None:
        columns = out.select_dtypes(include=np.number).columns

    if method == "ffill":
        out[columns] = out[columns].ffill()
        if allow_bfill:
            out[columns] = out[columns].bfill()
    elif method == "median":
        for c in columns:
            out[c] = out[c].fillna(out[c].median())
    elif method == "none":
        return out
    else:
        raise ValueError("method must be 'ffill', 'median', or 'none'")
    return out

def drop_missing(
    df: pd.DataFrame,
    columns=None,
    threshold: float | None = None,
    y_col: str | None = None,
) -> pd.DataFrame:
    """
    - If y_col is given, force-drop rows where y is missing (recommended).
    - If columns is given, drop rows missing in those columns.
    - Else if threshold is given (0..1), keep rows with at least threshold*#cols non-NaNs.
    - Else drop rows with any NaN.
    """
    out = df.copy()
    if y_col is not None:
        out = out.dropna(subset=[y_col])

    if columns is not None:
        return out.dropna(subset=list(columns))

    if threshold is not None:
        return out.dropna(thresh=int(np.ceil(threshold * out.shape[1])))

    return out.dropna()

def normalize_data(
    df: pd.DataFrame,
    columns=None,
    method: str = "standard",
    exclude: list[str] | None = None,
    return_scaler: bool = False,
):
    """
    Scale numeric **predictors**. Do NOT scale the target (e.g., VIG_ret) or date.
    - method='standard' -> StandardScaler (z-score)
    - method='minmax'   -> MinMaxScaler
    """
    out = df.copy()

    if columns is None:
        columns = out.select_dtypes(include=np.number).columns.tolist()

    exclude = set(exclude or [])
    cols = [c for c in columns if c not in exclude]

    if not cols:
        return (out, None) if return_scaler else out

    scaler = StandardScaler() if method == "standard" else MinMaxScaler()
    out[cols] = scaler.fit_transform(out[cols])

    if return_scaler:
        return out, scaler
    return out
