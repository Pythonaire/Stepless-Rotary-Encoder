import logging
import RPi.GPIO as io
io.setmode(io.BCM)
io.setwarnings(False)
logging.basicConfig(level=logging.INFO, format="[%(module)s] %(message)s")

''' stepless Rotary Encoder = Minimum BounceTime
 PEC16-4020F-N0024 - it's the 4020F that is important - the second digit here (0) means STEPLESS
The next part, N0024 determine whether a SWITCH pin is included (N=NO, S=YES) and the 24 shows how many steps per revolution
Select GPIO Pins with the same default state (1 or 0) for state and direction! 

'''

class BOURNE:
    def __init__(self, statePin, directionPin, switchPin=None, rotaryCallback=None, switchCallback=None, rotaryBouncetime=10, switchBouncetime=200):
        self.statePin = statePin
        self.directionPin = directionPin
        self.switchPin = switchPin
        self.rotaryCallback = rotaryCallback
        self.switchCallback = switchCallback
        self.rotaryBouncetime = rotaryBouncetime
        self.switchBouncetime = switchBouncetime 
        io.setup(self.statePin, io.IN, pull_up_down=io.PUD_DOWN)
        io.setup(self.directionPin, io.IN, pull_up_down=io.PUD_DOWN)
        if None != self.switchPin:
            io.setup(switchPin, io.IN, pull_up_down=io.PUD_UP)

    def start(self):
        io.add_event_detect(self.statePin, io.RISING, callback=self._clockCallback, bouncetime=self.rotaryBouncetime)
        if None != self.switchPin:
            io.add_event_detect(self.switchPin, io.FALLING, callback=self._switchCallback, bouncetime=self.switchBouncetime)


    def stop(self):
        io.remove_event_detect(self.clockPin)
        if None != self.switchPin:
            io.remove_event_detect(self.switchPin)
        io.cleanup()

    def _clockCallback(self, pin):
        if io.input(self.statePin) == 1: #RISING
            if io.input(self.directionPin) == 1:
                self.rotaryCallback(+1)
            else:
                self.rotaryCallback(-1)
        
    def _switchCallback(self, pin):
        if None == self.switchPin:
            return
        if io.input(self.switchPin) == 0: #FALLING
            self.switchCallback()