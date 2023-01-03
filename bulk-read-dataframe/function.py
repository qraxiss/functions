from typing import Iterable
import pandas as pd


def read_data(filepath: str) -> list[pd.DataFrame, str]:
    # Get the file extension
    extension: str = filepath.split('.')[-1]

    # Read the data based on the file extension
    match extension:
        case 'csv':
            df = pd.read_csv(filepath)
        case 'xlsx':
            df = pd.read_excel(filepath)
        case 'json':
            df = pd.read_json(filepath)
        case other:
            raise ValueError(f'Unsupported file extension: {extension}')

    return df, extension


def bulk_read(filepaths: Iterable[str]) -> dict[str, pd.DataFrame]:
    dataframes = dict()
    for filepath in filepaths:
        try:
            df, extension = read_data(filepath)
        except FileNotFoundError:
            print(f'{filepath}: Not Found!')
        except ValueError:
            print(f'{filepath}: Unsupported Format!')
        # if not getting any error
        else:
            df_name = filepath.replace(f'.{extension}', '')
            dataframes[df_name] = df

    return dataframes
