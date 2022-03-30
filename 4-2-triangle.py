import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    num = 0
    isRising = True
    print("Set period: ")
    period = int(input())
    ps = period/256
    while True:
        time.sleep(ps)
        binary = dec2bin(num)
        GPIO.output(dac, binary)

        if num == 255:
            isRising = False
        elif num == 0:
            isRising = True
        
        if isRising:
            num += 1
        else:
            num -= 1

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup
