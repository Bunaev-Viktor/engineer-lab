import RPi.GPIO as GPIO

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    print("Enter number 0 to 255: ")
    while True:
        inp = input()
        if inp == "q":
            break
        
        inp = int(inp)
        if inp > 255:
            print("Number is too big")
            continue
        elif inp < 0:
            print("Number cannot be negative")
            continue

        voltage = 3.3/256 * inp
        num = decimal2binary(inp)
        GPIO.output(dac, num) 
        print(voltage)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup
