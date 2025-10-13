import pyautogui
import time

n = int(input("Enter a number: "))

print("You have 4 seconds to click on your typing area...")
time.sleep(4)

for i in range(1, n + 1):
    pyautogui.typewrite("#" * i, interval=0.25)
    pyautogui.press("enter")
