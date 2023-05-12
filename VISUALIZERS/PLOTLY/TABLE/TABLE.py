from flojoy import flojoy, DataContainer
import plotly.graph_objects as go


@flojoy
def TABLE(dc_inputs: list[DataContainer], params: dict):
    """Node creates a Plotly table visualization for a given input data container.

    Args:
    dc_inputs (list): A list of DataContainer object(s) containing the input data.
    params (dict): A dictionary containing the parameters needed for the visualization.

    Returns:
    DataContainer: A DataContainer object containing the generated visualization and the processed data.

    Raises:
    ValueError: If the input data container is not supported.
    """
    dc_input = dc_inputs[0]
    if dc_input.type in ["dataframe", "plotly"]:
        df = dc_input.m
        fig = go.Figure(
            data=[
                go.Table(
                    header=dict(values=list(df.columns)),
                    cells=dict(values=[df[col] for col in df.columns]),
                )
            ]
        )
        return DataContainer(type="plotly", fig=fig, m=df)
    else:
        raise ValueError("unsupported input type for Plotly TABLE node")
