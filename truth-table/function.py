import pandas as pd
import numpy as np
import string

def truth_table(n: int):
    def add_element(elements, element, count):
        element_ = lambda x : element
        elements.extend(list(map(element_, range(count))))

    size = 2**n

    table = []
    for i in map(lambda x: 2**x, range(n-1,-1,-1)):
        loop = int(size / i)
        table.append([])
        for j in range(loop):
            add_element(table[-1], j%2, i)

    df = pd.DataFrame(table).T
    df.columns = list(string.ascii_lowercase[:len(df.columns)])
    return df