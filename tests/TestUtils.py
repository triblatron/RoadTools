import operator
import re
from typing import Any


def assert_comparison(case, actual, expected, tolerance):
    if isinstance(actual, float) and isinstance(expected, float):
        case.assertAlmostEqual(actual, expected, delta=tolerance)

def find(obj:Any, path:str):
    attrs = path.split('.')
    for attr in attrs:
        m = re.match(r'(\w+)\[(\d+)]', attr)
        if m is not None:
            obj = operator.getitem(getattr(obj, m.group(1)),int(m.group(2)))
        else:
            obj = getattr(obj, attr)

    return None