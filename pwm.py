import time
from machine import Pin, PWM

pwm = PWM(Pin(15))  # GPO15  connect Logic Analyzer
pwm1 = PWM(Pin(25)) #LED Onboard LED

pwm.freq(100)  # 10ms
pwm1.freq(1000)  # 1ms for LED

duty = 0
direction = 1

while True: 
    #for i in range(256):
        duty += direction
        if duty > 10:
            duty = 10
            direction = -1
        elif duty < 0:
            duty = 0
            direction = 1
        pwm.duty_u16(duty * 6553)
        pwm1.duty_u16(duty * 6553)      # LED will show this output
        time.sleep(0.001)         # 1ms delay


