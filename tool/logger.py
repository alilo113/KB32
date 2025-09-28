def log_keystrokes(key):
    with open("keystrokes.log", "a") as log_file:
        log_file.write(f"{key}\n")
        log_file.flush()
