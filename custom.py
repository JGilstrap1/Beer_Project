import Adafruit_CharLCD as LCD
import time
import prof as prof
lcd = LCD.Adafruit_CharLCDPlate()

def StartCustom():
    y = CustomTemp()
    shit = CustomTemp().PickLow()
    cock = CustomTemp().PickHigh()
    lcd.clear()
    prof.TempProfile().StartProfile(cock,shit)

class CustomTemp():
    
    def __init__(self):
        self.DefaultHigh = 40
        self.DefaultLow = 40
        
    def PickLow(self):
        lcd.clear()
        lcd.message(' Pick Low Value \n       %d       ' % (self.DefaultLow))
        while 1:
            if lcd.is_pressed(LCD.UP):
                self.DefaultLow += 1
                lcd.message(' Pick Low Value \n       %d       ' % (self.DefaultLow))
                
            if lcd.is_pressed(LCD.DOWN):
                self.DefaultLow -= 1
                lcd.message(' Pick Low Value \n       %d       ' % (self.DefaultLow))
                
            if lcd.is_pressed(LCD.SELECT):
                lcd.clear()
                return self.DefaultLow
                break
                
    def PickHigh(self):
        lcd.clear()
        lcd.message(' Pick High Value \n       %d       ' % (self.DefaultHigh))
        while 1:
            if lcd.is_pressed(LCD.UP):
                self.DefaultHigh += 1
                lcd.message(' Pick High Value \n       %d       ' % (self.DefaultHigh))
                
            if lcd.is_pressed(LCD.DOWN):
                self.DefaultHigh -= 1
                lcd.message(' Pick High Value \n       %d       ' % (self.DefaultHigh))
                
            if lcd.is_pressed(LCD.SELECT):
                lcd.clear()
                return self.DefaultHigh
                break
