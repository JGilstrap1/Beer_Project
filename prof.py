import temperature_sensor as temp
import Adafruit_CharLCD as LCD
import time
import relay as relay
import threading
import color as color
import utils
import toggle as tog
from constants import *
from custom import *
lcd = LCD.Adafruit_CharLCDPlate()

def CheckPage(Page):
    x = TempProfile()
    if Page == 1:
        #start ale temperatures
        x.StartProfile(Ale_High, Ale_Low)
    if Page == 2:
        #start lager temperatures
        x.StartProfile(Lager_High, Lager_Low)
    if Page == 3:
        #start diacetyl temperatures
        x.StartProfile(Diacetly_High, Diacetyl_Low)
    if Page == 4:
        #start cold lager temperatures
        x.StartProfile(Cold_Lager_High, Cold_Lager_Low)
    if Page == 5:
        #start custom temperatures
        #CustomTemp().StartCustom()
        StartCustom()

        


class TempProfile():
    
    def __init__(self):
        self.BreakToMenu = utils.ThreadSafeVar(False)
        self.BacklightOn = True
        self.temp_f = 0
    
    def Backlight(self, HighTemp, LowTemp):
        while 1:
            if self.BreakToMenu.get():
                break
            if lcd.is_pressed(LCD.RIGHT):
                time.sleep(0.3)
                if self.BacklightOn == True:
                    lcd.set_backlight(0)
                    self.BacklightOn = False
                else:
                    lcd.set_backlight(1)
                    if LowTemp < temp.temp_f < HighTemp:
                        color.GreenOnly()
                    else:
                        color.RedOnly()
                    self.BacklightOn = True
                        
    def CheckExit(self):
        while 1:
            if lcd.is_pressed(LCD.LEFT):
                time.sleep(0.3)
                self.BreakToMenu.set(True)
                lcd.clear()
                lcd.message(tog.MainMessage)
                relay.TurnOff()
                break

                    

    def StartProfile(self, HighTemp, LowTemp):
        threading.Thread(target=self.Backlight, args=(HighTemp, LowTemp,)).start()
        threading.Thread(target=self.CheckExit).start()
        while 1:
            temp.read_temp()
            if temp.temp_f >= HighTemp:
                if self.BacklightOn == True:
                    color.Red(str(temp.temp_f))
                relay.TurnOn()
                
            if temp.temp_f <= LowTemp:
                if self.BacklightOn == True: 
                    color.Red(str(temp.temp_f))
                relay.TurnOff()
            if LowTemp < temp.temp_f < HighTemp:
                if self.BacklightOn == True:
                    color.Green(str(temp.temp_f))
    
            i = 0
            while i < 5:
                i += 1
                if self.BreakToMenu.get():
                    return
                time.sleep(1)
         
        

