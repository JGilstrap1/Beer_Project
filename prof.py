import temperature_sensor as temp
import Adafruit_CharLCD as LCD
import time
import relay as relay
import threading
import color as color
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
        self.stopThread = False
        self.BreakToMenu = threading.Semaphore(1)
        
    def shouldStopThread(self):
        with self.BreakToMenu:
            return self.stopThread
        
    def setStopThread(self):
        with self.BreakToMenu:
            print("set stop thread to true")
            self.stopThread = True
    
    def Backlight(self):
        global BacklightOn
        while 1:
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
                        
    def CheckExit(self, BreakToMenu):
        global variable
        while 1:
            if lcd.is_pressed(LCD.LEFT):
                time.sleep(0.3)
                print("button pushed")
                self.setStopThread()
                if self.shouldStopThread():
                    with self.BreakToMenu:
                        variable = 1
                    

    def AleTemp(self):
        #variable = 0
        global input
        global BacklightOn
        BacklightThread = threading.Thread(target=self.Backlight,).start()
        ExitThread = threading.Thread(target=self.CheckExit, args=(self.BreakToMenu,)).start()
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
                
            
            with self.BreakToMenu:
                print("in break to menu")
                if variable == 1:
                    #variable = 0
                    #self.setStopThread()
                    #threading.Lock()
                    #if self.shouldStopThread():
                    print ("in break")
                    break
                    
            time.sleep(5)
        

