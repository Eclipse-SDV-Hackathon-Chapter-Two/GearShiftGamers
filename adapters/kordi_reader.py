import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import socket

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
x_channel = AnalogIn(ads, ADS.P0)
y_channel = AnalogIn(ads, ADS.P1)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.0.148', 65432)
client_socket.connect(server_address)

try:
    while True:
          movement = ""
          x_value = x_channel.value
          y_value = y_channel.value

          if x_value - 13180 > 20:
            print("right")
            movement = "right"

          if 13180 - x_value > 20:
            print("left")
            movement = "left"

          if y_value - 13044 > 20:
            print("jump")
            movement = "jump"

          if movement != "":
            client_socket.sendall(movement.encode())
          print(f"X: {x_value}, Y: {y_value}")
          time.sleep(0.1)
except KeyboardInterrupt:
    print("Program interrupted by user")

