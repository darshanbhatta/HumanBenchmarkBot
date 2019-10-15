from PIL import Image
import pytesseract
import pyautogui
import time
import webbrowser

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract' #need to install tesseract, windows installer: https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-3.05.02-20180621.exe

allWords = []

webbrowser.open('https://www.humanbenchmark.com/tests/verbal-memory', new=2)

time.sleep(3) #time it takes for webbrowser to open, change this to match your pc
xStart = 951 #x pos center of the start button, change if you are using different res
yStart = 507 #y pos center of the start button, change if you are using different res
xSeen = 870 #x pos center of the seen button, change if you are using different res
ySeen = 446 #y pos center of the seen button, change if you are using different res
xNew = 1038 #x pos center of the new button, change if you are using different res
yNew = 444 #y pos center of the new button, change if you are using different res
delay = .35 #change this for delay in seconds between each round
lvls = 100 #change this to match how many lvls you want the bot to do

pyautogui.click(xStart, yStart)
time.sleep(.5)

color = pyautogui.pixel(xStart, yStart)
hexColor = '%02x%02x%02x' % color
print(hexColor)
if(hexColor=='0089ce'):
    for num in range(lvls):
        # takes picture of the word
        im1 = pyautogui.screenshot(region=(xSeen-280,ySeen-154, 690, 75))
        # converts image of word into text
        word = pytesseract.image_to_string(im1)
    
        # checks if word is in the list of stored words and acts accordingly
        if word not in allWords:
            allWords.append(word)
            pyautogui.click(xNew, yNew)
        else:
            pyautogui.click(xSeen, ySeen)
    
        time.sleep(delay)
else:
    pyautogui.alert(text='Please have the tab fullscreened on your primary monitor, values may not work for resolutions other than 1920 by 1080', title='Game not detected!', button='Ok')





