import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()


def Green(Temp):
    lcd.clear()
    lcd.set_color(0.0,1.0,0.0)
    lcd.message(Temp)
    lcd.set_color(0.0,1.0,0.0)
    
    
def Yellow(Temp):
    lcd.clear()
    lcd.set_color(1.0,1.0,0.0)
    lcd.message(Temp)
    lcd.set_color(1.0,1.0,0.0)
    
def Red(Temp):
    lcd.clear()
    lcd.set_color(1.0,0.0,0.0)
    lcd.message(Temp)
    lcd.set_color(1.0,0.0,0.0)

def Blue(Temp):
    lcd.clear()
    lcd.set_color(1.0,1.0,1.0)
    lcd.message(Temp)
    lcd.set_color(1.0,1.0,1.0)
    
def GreenOnly():
    lcd.set_color(0.0,1.0,0.0)
    
def RedOnly():
    lcd.set_color(1.0,0.0,0.0)
    