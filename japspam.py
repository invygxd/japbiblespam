import pyautogui, time

time.sleep(10)

s = open(r"*ENTER japbible.txt FILE LOCATION HERE* \japbible.txt", "r")

for word in s:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
