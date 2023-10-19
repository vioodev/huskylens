import json
import time
import RPi.GPIO as GPIO

from huskylib import HuskyLensLibrary

def prettyPrintObject(object):
    count = 1
    if type(object) == list:
        for i in object:
            print("\t " + ("BLOCK_" if i.type == "BLOCK" else "ARROW_") + str(count) + " : " + json.dumps(i.__dict__))
            count += 1
    else:
        print("\t " + ("BLOCK_" if object.type == "BLOCK" else "ARROW_") + str(count) + " : " + json.dumps(
            object.__dict__))

def loopObjects():
    while True:
        try:
            prettyPrintObject(husky.getObjectByID(0))
        except IndexError:
            print("No object found.")
        time.sleep(0.5)


husky = HuskyLensLibrary("I2C", "", 0x32)
husky.algorthim("ALGORITHM_OBJECT_RECOGNITION")

while True:
    try:
        userInput = input("Press X to start the process.\n")

        if userInput == "X":
            husky.learn(0)
            time.sleep(3)
            loopObjects()
    except KeyboardInterrupt:
        print("Quitting.")
        quit()
