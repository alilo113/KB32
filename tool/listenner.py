from pynput import keyboard

file_name = "log.txt"

def on_press(key):
        try:
            print(f"Key pressed: {key.char}")
        except AttributeError:
            print(f"Special key pressed: {key}")

# Start listening
with keyboard.Listener(on_press=on_press) as listener:
    print("Listening...")
    listener.join()
