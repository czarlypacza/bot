111799
111800
import pyautogui
import time

# Move and click the input box
pyautogui.moveTo(2000, 650)  # Update coordinates as needed


n = 0
while n <= 888889:
    # Click the input box
    pyautogui.click()
    # Type the 6-digit code
    pyautogui.typewrite(str(111780 + n))
    # Press enter
    pyautogui.press("enter")
    # Wait for a short period to avoid overwhelming the system
    print("checked "+ str(111780 + n))
    n += 1
    time.sleep(0.1)

