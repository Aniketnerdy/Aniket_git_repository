import pyautogui,time
time.sleep(5)
pyautogui.screenshot("screen image.jpeg")
cordinates=pyautogui.locateCenterOnScreen("alarm_window.JPG")
print(cordinates)
pyautogui.moveTo((300,300),duration=2)