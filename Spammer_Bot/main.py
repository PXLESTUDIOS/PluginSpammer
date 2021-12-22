#imports/mods (plugins will tell you the import path. ex: pluginFileName.Plugin)
import pyautogui
import keyboard
import time
#import TheSong


#vars, in lyrics enter the other songs seperated with a comma [,]
LYRICS = "Nike Ticks, The Song"
STARTING_KEY = 'space'

#creator songs:
def creator():
    
    
    TEXT = open("Spammer_Bot\\Nike_Ticks.txt")
    print(f"Press [{STARTING_KEY}] when ready.")
    while True:
        if keyboard.is_pressed(STARTING_KEY):
            time.sleep(11)
            line = 0
            for each_line in TEXT:
                pyautogui.typewrite(each_line)
                pyautogui.press('enter')
                line =+1
                time.sleep(0.7)
            if line == 90:
                spammer()
            

#In plugin section you may enter the caller in the text document ex: phonk_song()

def spammer():
    #Starter
    type = input(f"Songs: {LYRICS}, Enter in the one you want.\n")
    #Plugins
    if type.lower() == 'the song':
        print(f"Press [{STARTING_KEY}] when ready.")
        #TheSong.boot()
    #Creator
    if type.lower() == 'nike ticks':
        creator()
spammer()












    
    