from flojoy import flojoy, OrderedPair
from typing import Optional
import serial
import numpy as np


@flojoy(deps={"pyserial": "3.5"})
def SERIAL_SINGLE_MEASUREMENT(
    default: Optional[OrderedPair] = None,
    comport: str = "/dev/ttyUSB0",
    baudrate: int = 9600,
) -> OrderedPair:
    """The SERIAL_SINGLE_MEASUREMENT node takes a single reading of data from an Ardunio or a similar serial device.

    Parameters
    ----------
    baudrate : int
        Baud rate for the serial communication.
    comport : string
        Defines the comunication port on which the serial device is connected.
    """

    ser = serial.Serial(comport, timeout=1, baudrate=baudrate)
    s = ""
    while s == "":
        s = ser.readline().decode()

    reading = s[:-2].split(",")
    reading = np.array(reading)  # Create an array
    reading = reading.astype("float64")  # Convert the array to float
    x = np.arange(0, reading.size)  # Create a second array

    return OrderedPair(x=x, y=reading)
