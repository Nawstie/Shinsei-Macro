import time
import pyautogui
import keyboard
import pygetwindow as gw
import pydirectinput as pdi
running = False
pdi.PAUSE = 0.045
locations = {
    "Fireball": 'Screenshots/Fireball.png',
    "Phoenix": 'Screenshots/PhoenixFlower.png',
    "EarthWall": 'Screenshots/EarthWall.png',
    "RockFist": 'Screenshots/RockFist.png',
    "StonePistol": 'Screenshots/StonePiss.png',
    "MudRiver": 'Screenshots/MudRiver.png'
}
while True:
    if keyboard.is_pressed("F8"): # checks if f8 is pressed
        running = not running # checks if the macro is running or not
        print("Macro ON" if running else "Macro OFF") 
        time.sleep(0.3)  # prevents double toggles
    if running: # if its true then it will run the macro
        window = gw.getActiveWindow() # gets the active window
        if window and window.title == "Roblox": # checks if the active window is Roblox
             #this will check if the image is on the screen and if it is then it will click on it and write "zvcb" in the chat
                for name, path in locations.items(): # this loops through the dictionary and gets the name and path of the image
                    try: #The reason for using try and except is to prevent the program from crashing if the image is not found on the screen
                        location = pyautogui.locateOnScreen(path, confidence=0.97) # this checks if the image is on the screen
                        print(location) # prints the location of the image
                    except Exception as e:
                        print(f"Error locating {name}: {e}")
                        continue

                    if not location: #The reason for using if not location is to check if the image is not found on the screen
                        print(f"{name} Not Found") # if the image is not found then it will print the name of the image and "Not Found"
                        continue
                    if name == "EarthWall": # checks if the name of the image is EarthWall
                        time.sleep(0.378) # waits for 0.1 seconds
                        for key in ['c','v','c']:
                            pdi.keyDown(key); pdi.keyUp(key)
                        pdi.click()
                        continue

                    if name == "StonePistol": # checks if the name of the image is StonePistol
                        time.sleep(0.378) # waits for 0.1 seconds
                        for key in ['c','v','b','x']:
                            pdi.keyDown(key); pdi.keyUp(key)
                        pdi.click()
                        continue

                    if name == "RockFist":
                        time.sleep(0.378) # waits for 0.1 seconds
                        for key in ['c','v','b','c']:
                            pdi.keyDown(key); pdi.keyUp(key)
                        pdi.click()
                        continue

                    if name == "MudRiver": # checks if the name of the image is MudRiver
                        time.sleep(0.378) # waits for 0.1 seconds
                        for key in ['c','v','z','x']:
                            pdi.keyDown(key); pdi.keyUp(key)
                        pdi.click()
                        continue

                    if name == "Phoenix": # checks if the name of the image is Phoenix
                        time.sleep(0.378) # waits for 0.1 seconds
                        for key in ['z','v','x','z']:
                            pdi.keyDown(key); pdi.keyUp(key)
                        pdi.click()
                        continue

                    if name == "Fireball": # checks if the name of the image is Fireball
                        time.sleep(0.378) # waits for 0.1 seconds
                        for key in ['z','v','c','b']:
                            pdi.keyDown(key); pdi.keyUp(key)
                        pdi.click()
                        continue
        else:
            print("Roblox is not the active window.")
        
