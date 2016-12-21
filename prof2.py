import temperature_sensor as temp
import Adafruit_CharLCD as LCD
import time
import relay as relay
import threading
import color as color
import utils
lcd = LCD.Adafruit_CharLCDPlate()

Ale_High = 70
Ale_Low = 65
Lager_High = 55
Lager_Low = 50
Diacetly_High = 68
Diacetyl_Low = 65
Cold_Lager_Low = 35
Custom_High = 0
Custom_low = 0
global input
variable = 0
input = 2
BacklightOn = True

def CheckPage(Page):
    x = TempProfile()
    if Page == 1:
        x.AleTemp()
        


class TempProfile():
    
    def __init__(self):
        self.BreakToMenu = utils.ThreadSafeVar(False)
        
    
    def Backlight(self):
        global BacklightOn
        while 1:
            if self.BreakToMenu.get():
                break
            if lcd.is_pressed(LCD.RIGHT):
                time.sleep(0.4)
                if BacklightOn == True:
                    print("if true")
                    lcd.set_backlight(0)
                    BacklightOn = False
                else:
                    print("if false")
                    lcd.set_backlight(1)
                    BacklightOn = True
                        
    def CheckExit(self):
        while 1:
            if lcd.is_pressed(LCD.LEFT):
                time.sleep(0.3)
                print("button pushed")
                self.BreakToMenu.set(True)
                break

                    

    def AleTemp(self):
        #variable = 0
        global input
        global BacklightOn
        threading.Thread(target=self.Backlight).start()
        threading.Thread(target=self.CheckExit).start()
        while 1:
            lcd.clear()
            temp.read_temp()
            lcd.message(str(temp.temp_f))
            if temp.temp_f >= Ale_High:
                if BacklightOn == True:  
                    color.Red()
                relay.TurnOn()
                
            if temp.temp_f <= Ale_Low:
                if BacklightOn == True:  
                    color.Red()
                relay.TurnOff()
            #if Ale_Low < temp.temp_f < Ale_High:
                #color.Green(input)
                #Don't adjust fridge
                
            i = 0
            while i < 5:
                i += 1
                if self.BreakToMenu.get():
                    print("in ale temp break")
                    return
                time.sleep(1)
         
        

