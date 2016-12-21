import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.output(23, GPIO.LOW)

#def TurnOn():
#    GPIO.output(23, GPIO.LOW)
 
def TurnOn():
    GPIO.output(23, GPIO.HIGH)

def TurnOff():
    GPIO.output(23, GPIO.LOW)
    
    