import webbrowser
import pyautogui
import time
webbrowser.open_new_tab("gmail.com")
search_item = pyautogui.prompt(text="", title="Gmail_search")
res = pyautogui.locateCenterOnScreen("image.png")
pyautogui.moveTo(res)
pyautogui.click()
pyautogui.write(search_item)
pyautogui.hotkey("enter")
str = pyautogui.prompt(text="", title="Number of times to repeat")
i = int(str)
n = 0
while(n < i):
    time.sleep(3)
    check = pyautogui.locateCenterOnScreen("check.png")
    pyautogui.moveTo(check)
    pyautogui.click()
    time.sleep(1)
    check = pyautogui.locateCenterOnScreen("delete.png")
    pyautogui.moveTo(check)
    pyautogui.click()
    n+= 1


