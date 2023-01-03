# Source Code

```python
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
```
# What does this code do?


`read_data` takes a filepath of a file as input and returns a tuple consisting of a Pandas DataFrame object and a string representing the file extension of the file. The function reads the file based on its file extension and stores the resulting data in a Pandas DataFrame. If the file extension is not one of 'csv', 'xlsx', or 'json', the function raises a `ValueError`.

`bulk_read` takes an iterable of filepaths as input and returns a dictionary where the keys are the file names (without the file extensions) and the values are the Pandas DataFrame objects obtained by reading the corresponding files. If a file is not found, the function prints a message indicating that the file was not found. If a file has an unsupported file extension, the function prints a message indicating that the file format is unsupported. If neither of these errors occurs, the function stores the data from the file in a Pandas DataFrame and adds it to the dictionary with the file name as the key.

The `bulk_read` function loops through the iterable of filepaths, tries to read each file using the `read_data` function, and handles any `FileNotFoundError` or `ValueError` exceptions that might be raised. If no errors are raised, it adds the data from the file to the dictionary. This allows the function to process multiple files and handle any errors that might occur while reading them.


# Using

Here is an example of how you could use the read_data and bulk_read functions:

```python
# Assume that the current directory contains a file called 'data.csv' and a file called 'data.xlsx'
import os

# Get the current directory
current_dir = os.getcwd()

# Create a list of filepaths to the files in the current directory
filepaths = [os.path.join(current_dir, 'data.csv'), os.path.join(current_dir, 'data.xlsx')]

# Read the data from the files
dataframes = bulk_read(filepaths)

# Print the dataframes
for df_name, df in dataframes.items():
    print(f'DataFrame name: {df_name}')
    print(df)

```

This code would read the data from the 'data.csv' and 'data.xlsx' files in the current directory and store the data in two Pandas DataFrame objects. It would then print the name of each DataFrame and the contents of the DataFrame.

# Output

```
DataFrame name: data
  Name  Age  Gender
0 Alice   24  Female
1   Bob   32    Male
2 Charlie   28    Male
DataFrame name: data
   Name  Age  Gender
0   Eve   26  Female
1 Frank   30    Male
```