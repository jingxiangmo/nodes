import pandas as pd
import io
import boto3
import keyring
from flojoy import flojoy, DataFrame


@flojoy
def READ_S3(
    s3_name: str = "",
    bucket_name: str = "",
    file_name: str = "",
) -> DataFrame:
    """The READ_S3 node takes a S3_key name, S3 bucket name, and file name as input, and extracts the file from the specified bucket using the S3_key that was saved.

    Inputs
    ------
    default: None

    Parameters
    ----------
    s3_name : str
        name of the key that the user used to save access and secret access key
    bucket_name : str
        AWS S3 bucket name that they are trying to access
    file_name : str
        name of the file that they want to extract

    Returns
    -------
    DataFrame
        DataFrame loaded from file in the specfied bucket

    """

    if s3_name == "":
        raise ValueError("Provide a name that was used to set AWS S3 key")

    try:
        accessKey = keyring.get_password("system", f"{s3_name}_ACCESSKEY")
        secretKey = keyring.get_password("system", f"{s3_name}_SECRETKEY")
        s3 = boto3.resource(
            "s3", aws_access_key_id=accessKey, aws_secret_access_key=secretKey
        )
        object = s3.Object(bucket_name, file_name)
        buffer = io.BytesIO()
        object.download_fileobj(buffer)
        df = pd.read_parquet(buffer)

        return DataFrame(df=df)

    except Exception as e:
        print(e)
