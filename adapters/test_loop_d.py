import uinput
import time

# Define the input device and the keys you want to simulate
device = uinput.Device([uinput.KEY_D])

# Simulate pressing and releasing the "d" key
def press_key_d():
    print("Simulating key press: 'd'")
    device.emit_click(uinput.KEY_D)  # Press and release the 'd' key

if __name__ == "__main__":
    try:
        while True:
            press_key_d()
            time.sleep(1)  # Delay between presses for testing purposes
    except KeyboardInterrupt:
        print("Simulation stopped.")