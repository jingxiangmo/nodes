from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np
from collections import namedtuple
from typing import Literal

import scipy.stats


@flojoy(node_type="default")
def SHAPIRO(
    default: OrderedPair | Matrix,
    select_return: Literal["statistic", "p-value"] = "statistic",
) -> OrderedPair | Matrix | Scalar:
    """The SHAPIRO node is based on a numpy or scipy function.
    The description of that function is as follows:

            Perform the Shapiro-Wilk test for normality.

            The Shapiro-Wilk test tests the null hypothesis that the
            data was drawn from a normal distribution.

    Parameters
    ----------
    select_return : This function has returns multiple objects:
            ['statistic', 'p-value']. Select the desired one to return.
            See the respective function docs for descriptors.
    x : array_like
            Array of sample data.

    Returns
    ----------
    DataContainer:
            type 'ordered pair', 'scalar', or 'matrix'
    """

    result = scipy.stats.shapiro(
        x=default.y,
    )

    return_list = ["statistic", "p-value"]
    if isinstance(result, tuple):
        res_dict = {}
        num = min(len(result), len(return_list))
        for i in range(num):
            res_dict[return_list[i]] = result[i]
        result = res_dict[select_return]
    else:
        result = result._asdict()
        result = result[select_return]

    if isinstance(result, np.ndarray):
        result = OrderedPair(x=default.x, y=result)
    elif isinstance(result, np.float64 | float | np.int64 | int):
        result = Scalar(c=float(result))

    return result
