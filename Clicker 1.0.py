import pyautogui
import keyboard
import time
import threading

# Global variables
clicking = False
click_type = 'left'  # 'left' or 'right'
click_position = (0, 0)

def clicker():
    global clicking
    while True:
        if clicking:
            pyautogui.click(*click_position, button=click_type)
            time.sleep(delay)

def start_stop_clicking():
    global clicking
    clicking = not clicking
    if clicking:
        print("Clicking started...")
    else:
        print("Clicking stopped...")

# Get user input for delay
delay = float(input("Enter delay between clicks in seconds: "))
click_type = input("Enter click type (left/right): ").lower()

# Get click position
set_position = input("Do you want to set a specific click position? (y/n): ").lower()
if set_position == 'y':
    print("Move your mouse to the desired position and press 'Enter'...")
    keyboard.wait('enter')
    click_position = pyautogui.position()
else:
    click_position = (0, 0)  # Default position

# Set hotkeys
keyboard.add_hotkey('s', start_stop_clicking)

# Start clicking thread
clicking_thread = threading.Thread(target=clicker, daemon=True)
clicking_thread.start()

print("Press 's' to start/stop clicking. Press 'esc' to exit.")

# Keep the program running
keyboard.wait('esc')  # Press 'esc' to exit the program
