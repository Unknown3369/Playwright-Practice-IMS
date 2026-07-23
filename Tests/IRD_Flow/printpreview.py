import time

def close_print_preview(page):
    print("Closing Chrome Print Preview...")

    time.sleep(20)
    
    page.keyboard.press("esc")
    print("Escape Pressed")

    time.sleep(3)

    print("Chrome Print Preview closed")