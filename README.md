# Stepless-Rotary-Encoder in python

## Description

Stepless rotary encoder are more handy and convinced as typical steping rotary encoder. In this example a BOURNE PEC16-4020F-N0024 is used with a raspberry pi. If you use other Pins, make sure, you set the right pull resistors and RISING/FALLING events.




````python3
from encoder import BOURNE
import logging


logging.basicConfig(level=logging.INFO, format="[%(module)s] %(message)s")

VolumeStatePin = 6    # pin 31 - (BCM12) standard IN value 0
VolumeDirectionPin = 26    # pin 37 - (BCM26) standard IN value 0
On_Off = 5    # pin 29 - OnOff(BCM5), standard IN value 1

def Vol(direction):
    logging.info("direction: {0}".format(direction))
    .....

def Switch():
    logging.info("State:")
    ....


Rotary = BOURNE(VolumeStatePin, VolumeDirectionPin, On_Off, Vol, Switch)
Rotary.start()
``````