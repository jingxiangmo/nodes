import numpy as np
from flojoy import flojoy, OrderedPair, Scalar, Vector
from nodes.TRANSFORMERS.ARITHMETIC.utils.arithmetic_utils import get_val
from functools import reduce


@flojoy
def ADD(
    a, b: list
):
    """Add 2 or more numeric arrays, matrices, dataframes, or constants element-wise.
    When a constant is added to an array or matrix, each element in the array or
    matrix will be increased by the constant value. If 2 arrays or matrices of different
    sizes are added, the output will be the size of the larger array or matrix with
    only the overlapping elements changed.
    """
    initial = get_val(a)
    seq = map(lambda dc: get_val(dc), b)
    y = reduce(lambda u, v: np.add(u, v), seq, initial)

    if isinstance(a, OrderedPair):
        return OrderedPair(x=a.x, y=y)
    elif isinstance(a, Vector):
        return Vector(v=y)
    elif isinstance(a, Scalar):
        return Scalar(c=y)
