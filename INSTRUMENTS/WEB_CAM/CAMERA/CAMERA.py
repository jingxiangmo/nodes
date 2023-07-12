import cv2
import os
from flojoy import flojoy, DataContainer
from typing import Optional
from PIL import Image
import numpy as np


@flojoy
def CAMERA(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The CAMERA node acquires an image using the selected camera.
    If no camera is detected, an error would be thrown.

    Parameters:
    ----------
    camera_ind : int
        Camera index (i.e. camera identifier)
    resolution : select
        Camera resolution. Choose from a few options.

    Returns:
    ----------
    DataContainer:
        type 'image'
    """
    camera_ind: int = params["camera_ind"]
    resolution: str = params["resolution"]

    try:
        camera = cv2.VideoCapture(camera_ind)
        if resolution != "default":
            resolution = resolution.split("x")
            try:
                camera.set(cv2.CAP_PROP_FRAME_WIDTH, int(resolution[0]))
                camera.set(cv2.CAP_PROP_FRAME_HEIGHT, int(resolution[1]))
            except cv2.error as camera_error:
                print(f"Invalid resolution ({resolution}). Try a lower value.")
                raise camera_error

        if not camera.isOpened():
            raise cv2.error("Failed to open camera")

        result, BGR_img = camera.read()

        if not result:
            raise cv2.error("Failed to capture image")
        camera.release()
        del camera

        RGB_img = cv2.cvtColor(BGR_img, cv2.COLOR_BGR2RGB)

        # Split the image channels
        red_channel = RGB_img[:, :, 0]
        green_channel = RGB_img[:, :, 1]
        blue_channel = RGB_img[:, :, 2]

        if RGB_img.shape[2] == 4:
            alpha_channel = RGB_img[:, :, 3]
        else:
            alpha_channel = None

        return DataContainer(
            type="image",
            r=red_channel,
            g=green_channel,
            b=blue_channel,
            a=alpha_channel,
        )

    except cv2.error as camera_error:
        raise camera_error
