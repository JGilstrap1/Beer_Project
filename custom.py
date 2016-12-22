import Adafruit_CharLCD as LCD
import time
#import prof
lcd = LCD.Adafruit_CharLCDPlate()


class CustomTemp():
    
    def __init__(self):
        self.DefaultHigh = 40
        self.DefaultLow = 40
        self.HighValue = 0
        self.LowValue = 0
        
    
    def PickLow(self):
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
                self.LowValue = self.DefaultLow
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
                self.HighValue = self.DefaultLow
                break
y = CustomTemp()
y.PickLow()
y.PickHigh()
lcd.clear()
StartProfile(self.LowValue,self.HighValue)