import temperature_sensor as temp
import Adafruit_CharLCD as LCD
import time
import relay as relay
import threading
import color as color
import utils
lcd = LCD.Adafruit_CharLCDPlate()

color.Red()
time.sleep(5)
color.Red()
time.sleep(5)
lcd.message("eat shit")
time.sleep(5)
color.Red()
time.sleep(5)
lcd.clear()