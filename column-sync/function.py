from typing import Iterable
import pandas as pd


def column_sync(dataframes: Iterable[pd.DataFrame],
                pairs: Iterable[dict[int, str]]) -> list[pd.DataFrame]:
    if not len(pairs) == len(dataframes):
        raise ValueError("Length of pairs does not match length of dataframes")

    result_dataframes = list()
    for df, pair in zip(dataframes, pairs):
        df = df[df.columns[list(pair.keys())]].copy()
        df.columns = list(pair.values())
        result_dataframes.append(df)

    return result_dataframes
