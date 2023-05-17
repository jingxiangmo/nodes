from flojoy import flojoy, DataContainer
import pandas as pd
import numpy as np


@flojoy
def TESTING(dc_inputs):
    x = None
    if dc_inputs.__len__() > 0:
        x = dc_inputs[0].y
    y = np.linspace(0, 10, 50)
    result = DataContainer(x=x, y=y)
    return result


# (dc_inputs, params):
#     """
#     For testing purposes.
#     """

#     # d = {'col1': [1, 2], 'col2': [3, 4]}
#     # df = pd.DataFrame(data=d)
#     # result = DataContainer(df)

#     x = None
#     if dc_inputs.__len__() > 0:
#         x = dc_inputs[0].y
#     y = np.linspace(float(params["start"]), float(params["end"]), int(params["step"]))
#     result = DataContainer(x=x, y=y)

#     return result
