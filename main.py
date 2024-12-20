import os
import time
import pyautogui
import keyboard

def main():
    os.system("start cmd")  # Opens a command prompt
    time.sleep(1)  # Allow time for the command prompt to open

    print("Enter the key you want to press repeatedly:")
    key_to_press = input("Key: ")

    print("Enter the interval (in seconds) between key presses:")
    try:
        interval = float(input("Interval (seconds): "))
    except ValueError:
        print("Invalid interval. Please enter a number.")
        return

    print(f"Press 'o' at any time to stop the script.")

    try:
        while True:
            if keyboard.is_pressed('o'):
                print("Stopping script...")
                break

            pyautogui.press(key_to_press)
            time.sleep(interval)

    except KeyboardInterrupt:
        print("Script terminated by user.")

if __name__ == "__main__":
    main()