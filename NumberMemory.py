import pyautogui
import time
import webbrowser

webbrowser.open('https://www.humanbenchmark.com/tests/number-memory', new=2)
time.sleep(3) #time it takes for webbrowser to open, change this to match your pc

delay = 1 #change this for delay in seconds between each round
lvls = 100 #change this to match how many lvls you want the bot to do

width, height = pyautogui.size()
print(width, height)
width = int(width/2)
height = int(height/3)
color = pyautogui.pixel(width, height)
hexColor = '%02x%02x%02x' % color
print(hexColor)
if(hexColor=='0089ce'):
    x, y = pyautogui.locateCenterOnScreen('startnum.png')
    pyautogui.click(width, height+100)
    for w in range(lvls):
        # very simple just copies and pastes the number to the next page
        pyautogui.click(x=width, y=height,clicks=3,interval=.25)
        pyautogui.hotkey('ctrl', 'c')
        hexColor=''
        while(hexColor!='006ea5'):
            color = pyautogui.pixel(width, height)
            hexColor = '%02x%02x%02x' % color

        hexColor=''
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(delay)
        if(w!=lvls-1):
            pyautogui.click(x, y)
else:
    pyautogui.alert(text='Please have the tab fullscreened on your primary monitor, values may not work for resolutions other than 1920 by 1080', title='Game not detected!', button='Ok')




