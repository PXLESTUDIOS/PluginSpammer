import pyautogui
import keyboard
import time








def boot():
    
    TEXT = open("Spammer_Bot\\pluginBaseplate\\BaseplateSong.txt") #change BaseplateSong to whatever you want. If this doesnt work comment on the github project
    
    
        
    time.sleep(5)
    line = 0
    for each_line in TEXT:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')
    
        time.sleep(0.7)
            

