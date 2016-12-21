import temperature_sensor as temp
import Adafruit_CharLCD as LCD
import time
import relay as relay
import threading
import color as color
import utils
import toggle as tog
lcd = LCD.Adafruit_CharLCDPlate()

Ale_High = 70
Ale_Low = 65

def CheckPage(Page):
    x = TempProfile()
    if Page == 1:
        x.AleTemp()
        


class TempProfile():
    
    def __init__(self):
        self.BreakToMenu = utils.ThreadSafeVar(False)
        self.BacklightOn = True
        self.temp_f = 0
    
    def Backlight(self):
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
                    if Ale_Low < temp.temp_f < Ale_High:
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
                break

                    

    def AleTemp(self):
        threading.Thread(target=self.Backlight).start()
        threading.Thread(target=self.CheckExit).start()
        while 1:
            temp.read_temp()
            if temp.temp_f >= Ale_High:
                if self.BacklightOn == True:
                    color.Red(str(temp.temp_f))
                relay.TurnOn()
                
            if temp.temp_f <= Ale_Low:
                if self.BacklightOn == True: 
                    color.Red(str(temp.temp_f))
                relay.TurnOff()
            if Ale_Low < temp.temp_f < Ale_High:
                if self.BacklightOn == True:
                    color.Green(str(temp.temp_f))
    
            i = 0
            while i < 5:
                i += 1
                if self.BreakToMenu.get():
                    return
                time.sleep(1)
         
        

