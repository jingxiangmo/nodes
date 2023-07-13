from flojoy import OrderedPair, flojoy
import scipy.signal


@flojoy(node_type="default")
def DETREND(
    default: OrderedPair,
    axis: int = -1,
    type: str = "linear",
    bp: int = 0,
    overwrite_data: bool = False,
) -> OrderedPair:
    """The DETREND node is based on a numpy or scipy function.
    The description of that function is as follows:


            Remove linear trend along axis from data.

    Parameters
    ----------
    data : array_like
            The input data.
    axis : int, optional
            The axis along which to detrend the data. By default this is the
            last axis (-1).
    type : {'linear', 'constant'}, optional
            The type of detrending. If ``type == 'linear'`` (default),
            the result of a linear least-squares fit to `data` is subtracted
            from `data`.
            If ``type == 'constant'``, only the mean of `data` is subtracted.
    bp : array_like of ints, optional
            A sequence of break points. If given, an individual linear fit is
            performed for each part of `data` between two break points.
            Break points are specified as indices into `data`. This parameter
            only has an effect when ``type == 'linear'``.
    overwrite_data : bool, optional
            If True, perform in place detrending and avoid a copy. Default is False

    Returns
    ----------
    DataContainer:
            type 'ordered pair'"""
    result = OrderedPair(
        x=default.x,
        y=scipy.signal.detrend(
            data=default.y,
            axis=axis,
            type=type,
            bp=bp,
            overwrite_data=overwrite_data,
        ),
    )
    return result
