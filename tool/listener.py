from pynput import keyboard

def on_press(key):
    try:
        print(f'This Key {key.char} pressed')
    except AttributeError:
        print(f'The special key {key} pressed')

def on_release(key):
    if key == keyboard.Key.esc:
        print("Exiting...")
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    while on_press:
        print("Listening...")
        
    listener.join()
