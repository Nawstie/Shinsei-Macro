import time
import cv2
import numpy as np
import pyautogui
import keyboard
import pygetwindow as gw
import pydirectinput as pdi

running = False

# Use your actual cropped images here
locations = {
    "Fireball": "Screenshots/Fireball.png",
    "Phoenix": "Screenshots/PhoenixFlower.png"
}

def detect_image(template_path, threshold=0.75):
    # Load template
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    if template is None:
        print(f"[ERROR] Could not load template: {template_path}")
        return None

    w, h = template.shape[::-1]

    # Screenshot → grayscale
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)

    # Edge detection (makes shapes stand out)
    template_edges = cv2.Canny(template, 50, 150)
    screen_edges = cv2.Canny(screenshot, 50, 150)

    # Template matching
    result = cv2.matchTemplate(screen_edges, template_edges, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)

    for pt in zip(*loc[::-1]):
        return pt[0], pt[1], w, h  # x, y, width, height

    return None


print("Press F8 to toggle macro ON/OFF")

while True:
    if keyboard.is_pressed("F8"):
        running = not running
        print("Macro ON" if running else "Macro OFF")
        time.sleep(0.3)

    if running:
        window = gw.getActiveWindow()

        if window and "Roblox" in window.title:
            for name, path in locations.items():
                location = detect_image(path)

                print(f"{name}: {location}")

                if not location:
                    continue

                # Ability logic
                if name == "Phoenix":
                    for key in ['z','v','c','b']:
                        pdi.keyDown(key); pdi.keyUp(key)
                    pdi.click()
                    continue

                if name == "Fireball":
                    for key in ['z','v','c','b']:
                        pdi.keyDown(key); pdi.keyUp(key)
                    pdi.click()
                    continue

        else:
            print("Roblox is not the active window.")
            time.sleep(0.2)
