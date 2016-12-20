import time
import Adafruit_CharLCD as LCD
import commands
import psutil
import toggle as tog
import temperature_sensor as temp
from prof import CheckPage


lcd = LCD.Adafruit_CharLCDPlate()
#lcd.set_color(1.0, 1.0, 1.0)
global CurrentPage
CurrentPage = 0
i = 0
lcd.message("LOADING\n")

while (i<16):
    lcd.message(chr(219))
    time.sleep(0.1)
    i += 1
    
lcd.clear()
lcd.message("   Boner Brew   \n")
lcd.message("   Thermostat   ")

while 1:
    try:
        if lcd.is_pressed(LCD.RIGHT):
            if CurrentPage == 5:
                CurrentPage = 1
            else:
                CurrentPage += 1
            tog.DisplayMenu(CurrentPage)
                
        if lcd.is_pressed(LCD.LEFT):
            if CurrentPage == 0 | CurrentPage == 1:
                CurrentPage = 5
            else:
                CurrentPage -= 1
            tog.DisplayMenu(CurrentPage)
            #lcd.message(str(CurrentPage))

            
        if lcd.is_pressed(LCD.UP):
            lcd.clear()
            lcd.message(tog.MainMessage)
            
        if lcd.is_pressed(LCD.DOWN):
            lcd.clear()
            tog.DisplayMenu(CurrentPage)
            
        if lcd.is_pressed(LCD.SELECT):
            time.sleep(0.3)
            lcd.clear()
            CheckPage(CurrentPage)
            
##            if CurrentPage == 1:
##                print("how many")
##                CheckPage(CurrentPage)
##            if CurrentPage == 2:
##                LagerTemp()
##            if CurrentPage == 3: 
##                Diacetyl()
##            if CurrentPage == 4:
##                ColdLager()
##            if CurrentPage == 5:
##                Custom()

                
            
        
    except KeyboardInterrupt:
        lcd.message("Aborting...")
        time.sleep(2)
        lcd.clear()
        
        


            
        
      
    