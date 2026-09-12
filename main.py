
import time
import pyautogui
import pygetwindow as gw 
import pydirectinput as pdi


time.sleep(3) # waits for 3  seconds before starting the script
print(gw.getActiveWindow()) # prints the title of the active window
pdi.keyDown('z'); pdi.keyUp('z') # presses the z key down and then up
pdi.click()