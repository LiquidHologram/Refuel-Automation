from lib2to3.pgen2 import driver
from os import link
import keyboard
import webbrowser
import pyautogui
import win32com
import time

#Failsafe
pyautogui.FAILSAFE = True

link = "https://play.staratlas.com/fleet"
firefox = webbrowser.Mozilla("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
firefox.open(link)

#To get to wallet popup
time.sleep(3)
for i in range(5):
    keyboard.press_and_release('Tab')
    time.sleep(.3)
keyboard.press_and_release('Return')

#To open wallet
for i in range(2):
    keyboard.press_and_release('Tab')
    time.sleep(.3)
keyboard.press_and_release('Return')

#To login
time.sleep(2)
keyboard.write("PASSWORD")
keyboard.press_and_release('Return')

#Close popup wallet window
time.sleep(5)
close = pyautogui.locateCenterOnScreen('close.png')
pyautogui.click(close)

#Click manage fleet for first ship and resupply
time.sleep(3)
fleet = pyautogui.locateCenterOnScreen('manageFleet.png')
pyautogui.click(fleet)

time.sleep(1)
resupply = pyautogui.locateCenterOnScreen('resupply.png')
pyautogui.click(resupply)

#Submit payment for first resupply
time.sleep(10)
approve = pyautogui.locateCenterOnScreen('approve.png')
pyautogui.click(approve)

time.sleep(2)
pyautogui.click(1500, 370, 1, 0)


#Click manage fleet for second ship and resupply
time.sleep(2)
pyautogui.scroll(-10000)
time.sleep(3)
fleet = pyautogui.locateOnScreen('manageFleet.png', region=(1360, 888, 210, 70))
pyautogui.click(fleet)

time.sleep(1)
pyautogui.click(resupply)

#Submit payment for second resupply
time.sleep(10)
approve = pyautogui.locateCenterOnScreen('approve.png')
pyautogui.click(approve)

time.sleep(2)
pyautogui.click(1500, 409, 1, 0)


#time.sleep(1)
#pyautogui.scroll(10)

#exit()