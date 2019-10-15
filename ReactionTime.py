import pyautogui
import time
import webbrowser


webbrowser.open('https://www.humanbenchmark.com/tests/reactiontime', new=2)
time.sleep(3) #time it takes for webbrowser to open, change this to match your pc

delay = 0 #change this for delay in seconds
lvls = 5 #change this for the amount of levels you want the bot to complete

width, height = pyautogui.size()
print(width, height)
width = int(width/2)
height = int(height/4)
pyautogui.moveTo(width, height)
# gets the current hex color of the game
color = pyautogui.pixel(width, height)
hexColor = '%02x%02x%02x' % color
print(hexColor)
if(hexColor=='0089ce'):
    pyautogui.click()
    for x in range(lvls):
        # checks every time if the color is not green, when it is green it delays and then clicks the screen and waits for the next round
        while(hexColor!='18d971'):
            color = pyautogui.pixel(width, height)
            hexColor = '%02x%02x%02x' % color
        print(hexColor)
        time.sleep(delay)
        pyautogui.click()
        if(x!=4):
            pyautogui.click()
        
        hexColor = ''
else:
    pyautogui.alert(text='Please have the tab fullscreened on your primary monitor, values may not work for resolutions other than 1920 by 1080', title='Game not detected!', button='Ok')
