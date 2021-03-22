from machine import Pin, PWM
import time

pwm = PWM(Pin(25))# Construct PWM object, with LED on Pin(25).

pwm.freq(1000)# Set the PWM frequency.

duty = 0
direction = 1

#for i in range( 16 *256 ):
while True:
        duty += direction
        if duty > 255:
            duty = 255
            direction = -1
        elif duty < 0: 
            duty = 0
            direction = 1
        pwm.duty_u16(duty * duty)
        time.sleep(0.001)
