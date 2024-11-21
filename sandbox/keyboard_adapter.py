import keyboard

# Listen to all keypresses and print them
def log_key(event):
    print(f"Key {event.name} {'pressed' if event.event_type == 'down' else 'released'}")

keyboard.hook(log_key)

# Simulate pressing the "F" key after 2 seconds
keyboard.press_and_release('f')

# Keep the program running
keyboard.wait('esc')  # Press 'esc' to exit