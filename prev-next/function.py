from itertools import tee, islice, chain
from typing import Iterable

def previous_and_next(list_like: Iterable):
    prevs, items, nexts = tee(list_like, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(prevs, items, nexts)