# control_servo.py

import time
import math
import keyboard as kb
# import smbus2

import smbus
from Control_servo.ServoPCA9685 import  ServoPCA9685
from Control_servo.PCA9685 import  PCA9685

i2cbus = smbus2.SMBus(0)
pca = PCA9685.PCA9685(i2cbus)
s0 = ServoPCA9685.ServoPCA9685(pca, PCA9685.CHANNEL00)
s1 = ServoPCA9685.ServoPCA9685(pca, PCA9685.CHANNEL01)

UP = 'w'
DOWN = 's'
LEFT = 'a'
RIGHT = 'd'

delta = 1
UP_STOP = 510
DOWN_STOP = 130
LEFT_STOP = 130
RIGHT_STOP = 510

# pulsex = 130
# pulsey = 130
class Control_servo(object):
    def __init__(self, pulsex = 130, pulsey = 130):
        self.pulsex = pulsex
        self.pulsey = pulsey

    def setX(self, x):
        self.pulsex = x

    def setY(self, y):
        self.pulsey = y

    def getX(self):
        return self.pulsex

    def getY(self):
        return self.pulsey

    def __move_servo(self):
        if kb.is_pressed(UP) and self.pulsey + delta <= UP_STOP:
            self.pulsey += delta
        if kb.is_pressed(DOWN) and self.pulsey - delta >= DOWN_STOP:
            self.pulsey -= delta
        if kb.is_pressed(LEFT) and self.pulsex - delta >= LEFT_STOP:
            self.pulsex -= delta
        if kb.is_pressed(RIGHT) and self.pulsex + delta <= RIGHT_STOP:
            self.pulsex += delta
        s0.set_pulse(self.pulsex)
        s1.set_pulse(self.pulsey)

    def run(self):
        while True:
            self.__move_servo()
            print(f"pulsex: {self.pulsex}, pulsey: {self.pulsey}")
            time.sleep(0.005)  # Для избежания постоянного обновления
    def keyboard_control(self):
        while(True):
            # key = cv2.waitKey(5)
            delta = 1
            if kb.is_pressed('w'):
                self.pulsey += delta
            if kb.is_pressed('s'):
                self.pulsey -= delta
            if kb.is_pressed('a'):
                self.pulsex -= delta
            if kb.is_pressed('d'):
                self.pulsex += delta
            if kb.is_pressed('w') or kb.is_pressed('s') or kb.is_pressed('a') or kb.is_pressed('d'):
                print(self.pulsex, self.pulsey)
            time.sleep(0.005)

    def greet(self):
        print("Start")
