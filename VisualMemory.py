#!/usr/bin/python
# -*- coding: utf-8 -*-
import pyautogui
import time
import webbrowser
from PIL import Image

webbrowser.open('https://www.humanbenchmark.com/tests/memory', new=2)
time.sleep(3)  # time it takes for webbrowser to open in seconds, change this to match your pc
lvls = 115  # change this to match how many lvls you want the bot to do

(width, height) = pyautogui.size()
print (width, height)
width = int(width / 2)
height = int(height / 3)

color = pyautogui.pixel(width, height)
hexColor = '%02x%02x%02x' % color
print hexColor
if hexColor == '007bb9':
    pyautogui.click(width, height)
    time.sleep(.7)
    for w in range(lvls):

        img1 = pyautogui.screenshot(region=(width - 364, 280, 700, 445))
        xList = []
        yList = []

        # img1 = Image.open('my_screenshot.png')

        pix = img1.load()
        time.sleep(1)
        whiteCol = 0
        lastXAdded = 0
        oldLength = 0

        x = 0
        while x < img1.size[0]:

            for y in range(img1.size[1]):

                if pix[x, y] == (255, 255, 255) and whiteCol == 0:

                    if lastXAdded == 0 or lastXAdded + 1 != x:
                        xList.append(x)
                        yList.append(y)
                        whiteCol = 1
                    lastXAdded = x
                elif whiteCol == 1 and pix[x, y] != (255, 255, 255):

                    xList.append(x)
                    yList.append(y - 1)
                    whiteCol = 0

               # 108 126

            if len(xList) > oldLength:
                length = abs(yList[len(yList) - 1] - yList[len(yList)
                             - 2])
                x += length + int(.32 * length)
                oldLength = len(xList)
            else:
                x += 1

           # pyautogui.click(width-364+x,280+y)

        print xList
        print yList

        x = 0
        while x < len(xList):
            if x + 1 < len(xList) and xList[x + 1] == xList[x]:

        # print(x, x+1, yList[x+1], yList[x], xList[x], xList[x+1])

                yAvg = int((yList[x + 1] + yList[x]) / 2)
                xAvg = int((xList[x] + xList[x + 1] + yList[x + 1]
                           - yList[x]) / 2) + 1

                # print(xAvg, yAvg)

                x += 2
                pyautogui.click(width - 364 + xAvg, 280 + yAvg)
                time.sleep(.05)
        time.sleep(1.85)
else:
    pyautogui.alert(text='Please have the tab fullscreened on your primary monitor, values may not work for resolutions other than 1920 by 1080'
                    , title='Game not detected!', button='Ok')
