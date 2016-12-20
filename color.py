import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()


def Green():
    #if input %2 == 0:
    lcd.set_color(0.0,1.0,0.0)
    
def Yellow():
    #if input %2 == 0:
    lcd.set_color(1.0,1.0,0.0)
    
def Red():
##    print ("in Red")
##    print input
##    if input %2 == 0:
    lcd.set_color(1.0,0.0,0.0)
    

