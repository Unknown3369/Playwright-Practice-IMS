import time



def close_print_preview():
    print("Closing Chrome Print Preview...")

    time.sleep(20)
    
    import pyautogui
    pyautogui.press("esc")

    time.sleep(3)

    print("Chrome Print Preview closed")