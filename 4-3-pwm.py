import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)

p = GPIO.PWM(24, 1000)
t = GPIO.PWM(2, 1000)

try:
    dc = 0
    voltage = 0
    print("Set you duty cycle: ")
    while True:
        dc = int(input())
        p.start(dc)
        t.start(dc)
        voltage = 3.3/100 * dc
        print(voltage)

finally:
    p.stop()
    t.stop()
    GPIO.cleanup()
