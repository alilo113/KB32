from pynput import keyboard

def on_release(key):
    if key == keyboard.Key.esc:
        print("Exiting...")
        return False

# Collect events until released
with keyboard.Listener(on_release=on_release) as listener:
    print("Listening...")
    listener.join()
