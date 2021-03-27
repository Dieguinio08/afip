import pyautogui

# Capturar pantalla.
img = pyautogui.screenshot()
# Guardar imagen.
#screenshot.save("screenshot.png")
# Mostrar imagen.
#screenshot.show()
# Capturar una porción de la pantalla.
#screenshot = pyautogui.screenshot(region=(50, 50, 400, 300))
print (img.getpixel((100, 200)))
pyautogui.moveTo(100, 100, duration = 0)
pyautogui.click(100, 100)
pyautogui.typewrite("hello Geeks !")
#https://www.geeksforgeeks.org/mouse-keyboard-automation-using-python/
pyautogui.hotkey("ctrlleft", "a")
pyautogui.typewrite(["a", "left", "ctrlleft"])

import pyautogui
from PIL import Image
from time import sleep
 
pyautogui.screenshot('current_screen.png')
img_a_pixels = Image.open('current_screen.png').getdata()
#sleep(60) #Used in practice
pyautogui.screenshot('current_screen.png')
img_b_pixels = Image.open('current_screen.png').getdata()
 
difference = 0
for pixel_a, pixel_b in zip(img_a_pixels, img_b_pixels):
    if pixel_a != pixel_b:
        difference += 1
print(difference)