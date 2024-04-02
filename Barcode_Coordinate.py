#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank,follow_for_ms
from ev3dev2.sensor import INPUT_1,INPUT_2,INPUT_3,INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sensor.lego import ColorSensor
from time import sleep

def coordinates(Shelving, Box):
    #Only returns the coordinate system no movement in (x,y) format
    NewCoordinates = [0,0]
    if Shelving == 'A1' or Shelving == 'B1':
        if Shelving =='A1':
            NewCoordinates = [0,6]
        else:
            NewCoordinates = [54,6]
    elif Shelving == 'A2' or Shelving == 'B2':
        if Shelving == 'A2':
            NewCoordinates = [0,30]
        else:
            NewCoordinates = [54,30]
    elif Shelving == 'C1' or Shelving == 'D1':
        if Shelving == 'C1':
            NewCoordinates = [0,54]
        else:
            NewCoordinates = [54,54]
    elif Shelving == 'C2' or Shelving == 'D2':
        if Shelving == 'C2':
            NewCoordinates = [0,78]
        else:
            NewCoordinates = [54,78]

    if (Box > 6) and (Shelving != 'C2' or Shelving != 'D2'):
        Yvalue= NewCoordinates[1] + 24
        NewCoordinates[1] =Yvalue
    
    if (Box == 2 or Box == 8):
        Xvalue = NewCoordinates[0]+6
        NewCoordinates[0] = Xvalue
    elif (Box == 3 or Box == 9):
        Xvalue = NewCoordinates[0]+12
        NewCoordinates[0] = Xvalue
    elif (Box == 4 or Box == 10 ):
        Xvalue = NewCoordinates[0]+18
        NewCoordinates[0] = Xvalue
    elif (Box == 5 or Box == 11):
        Xvalue = NewCoordinates[0] +24
        NewCoordinates[0] = Xvalue
    elif (Box == 6 or Box == 12):
        Xvalue = NewCoordinates[0] + 30
        NewCoordinates[0] = Xvalue


    return NewCoordinates


def barcode():
    #returns what barcode it reads
    Right_Moter = OUTPUT_B
    Left_Motor = OUTPUT_A
    gyro = GyroSensor(INPUT_2)
    #Initializing the robot 
    robotDrive = tank_drive = MoveTank(Right_Moter,Left_Motor)
    robotDrive.gyro = GyroSensor()
    robotDrive.gyro.calibrate()

    velocity = 15
    
    robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(30), target_angle = 0, follow_for = follow_for_ms, ms = time / 0.001)
    def Drive(distance):
        #returns what barcode it reads
        Right_Moter = OUTPUT_B
        Left_Motor = OUTPUT_A
        gyro = GyroSensor(INPUT_2)
        #Initializing the robot 
        robotDrive = tank_drive = MoveTank(Right_Moter,Left_Motor)
        robotDrive.gyro = GyroSensor()
        robotDrive.gyro.calibrate()
        velocity = 15
        time = distance/velocity
        robotDrive.follow_gyro_angle(kp = 11.3, ki = 0.05, kd = 3.2, speed = SpeedPercent(30), target_angle = 0, follow_for = follow_for_ms, ms = time / 0.001)

    color_sensor= ColorSensor() #initilize color sesnor

    def move_until_black(): #moves to black sensor to begin
        Drive(100)
        while True:
            if color_sensor.color == ColorSensor.COLOR_BLACK:
                break

    move_until_black()

    Drive(0.5)

    if color_sensor.color == ColorSensor.COLOR_BLACK:
        barcode ="Type 3"
        Drive(1)
    else:
        Drive(0.5)
        if color_sensor == ColorSensor.COLOR_BLACK:
            barcode = "Type 2"
            Drive(0.5)
        else:
            Drive(0.5)
            if color_sensor == ColorSensor.COLOR_BLACK:
                barcode = "Type 4"
            else:
                barcode = "Type 1"
    return barcode




