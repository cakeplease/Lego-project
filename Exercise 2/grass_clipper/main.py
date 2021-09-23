#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import sys


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.A)
on_off_sensor = TouchSensor(Port.S3)
obstacle_sensor = UltrasonicSensor(Port.S2)

robot = DriveBase(left_motor, right_motor, wheel_diameter=81.6, axle_track=115)
ev3.speaker.set_volume(200, "_all_")

# Write your program here.
on_off = False
while not on_off:
    if on_off_sensor.pressed():
        ev3.speaker.say("Exercise 2")
        wait(2000)
        on_off = True
    else:
        continue

while on_off:
    if on_off_sensor.pressed():
        robot.stop()       
        ev3.speaker.say("Exercise done.")
        sys.exit()  

    # Begin driving forward at 200 millimeters per second.
    robot.drive(200, 0)

    # Wait until an obstacle is detected. This is done by repeatedly
    # doing nothing (waiting for 10 milliseconds) while the measured
    # distance is still greater than 300 mm.
    while obstacle_sensor.distance() > 100:
        if on_off_sensor.pressed():
            robot.stop()
            ev3.speaker.say("Exercise done.")
            sys.exit()    

        wait(10)

    # Drive backward for 300 millimeters.
    robot.straight(-50)

    # Turn around by 120 degrees
    robot.turn(120)