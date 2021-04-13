import time
from machine import I2C
from machine import Pin
import numpy as np

# Le pin est à définir
# Doc : https://docs.micropython.org/en/latest/library/pyb.Pin.html
# TODO
wakePin = Pin(5, mode=Pin.IN)

accel_x = np.array[]
accel_y = np.array[]
accel_z = np.array[]

while (True):
    if wakePin == 0 :
        machine.deepsleep(10*1000)
    else :
        #On active tout le système
        #TODO









