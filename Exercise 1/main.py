# Exercise 1.
# Robot prints "Hello world" going in rectagular shape and says "Have a nice day".

#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialize the EV3 brick.
ev3 = EV3Brick()
# Initialize a motor at port B.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=115)

ev3.screen.print("Hello world.")
wait(5000)

robot.straight(200)
robot.turn(90)

robot.straight(400)
robot.turn(90)

robot.straight(200)
robot.turn(90)

robot.straight(400)
robot.turn(90)

ev3.speaker.say("Have a nice day")
