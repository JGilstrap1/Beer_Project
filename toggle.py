import time
import Adafruit_CharLCD as LCD
#import commands
#import psutil
#import toggle as tog

lcd = LCD.Adafruit_CharLCDPlate()
global CurrentPage

Message1 = "<      Ale     >\n<  Temperature >"
Message2 = "<     Lager    >\n< Fermentation >"
Message3 = "<   Diacetyl   >\n<     Rest     >"
Message4 = "<     Cold     >\n<     Lager    >"
Message5 = "<    Custom    >\n<  Temperature >"
MainMessage = "   Boner Brew   \n   Thermostat   "

def DisplayMenu(CurrentPage):
    #global CurrentPage
    lcd.clear()
    #lcd.message(Message)
    if CurrentPage == 1:
        lcd.clear()
        lcd.message(Message1)
    if CurrentPage == 2:
        lcd.clear()
        lcd.message(Message2)
    if CurrentPage == 3:
        lcd.clear()
        lcd.message(Message3)
    if CurrentPage == 4:
        lcd.clear()
        lcd.message(Message4)
    if CurrentPage == 5:
        lcd.clear()
        lcd.message(Message5)
    
    