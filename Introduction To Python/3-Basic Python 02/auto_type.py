import pyautogui
from time import sleep


sleep(5)
pyautogui.write("# Hello World!", interval=0.25)
pyautogui.press("enter")
pyautogui.press("enter")

# Hello World!

for i in range(1, 10):
    pyautogui.write(f"Loop Running: {i} time", interval=0.25)
    pyautogui.press("enter")
