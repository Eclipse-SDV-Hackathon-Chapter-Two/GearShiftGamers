import os
import time
import sys
from datetime import datetime
from kuksa_client.grpc import VSSClient
from kuksa_client.grpc import Datapoint

import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import socket
from parameters import joy_name_left, joy_name_right, joy_name_up

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
x_channel = AnalogIn(ads, ADS.P0)
y_channel = AnalogIn(ads, ADS.P1)

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_address = ('192.168.0.148', 65432)
# client_socket.connect(server_address)

# add = os.environ.get('KUKSA_DATA_BROKER_ADDR', '198.168.0.148')
# port = int(os.environ.get('KUKSA_DATA_BROKER_PORT', '55555'))
# mode = os.environ.get('SPEED_PROVIDE_MODE', 'webui')


# databroker_host = '127.0.0.1'
databroker_host = '192.168.0.148'
databroker_port = '55555'
client = VSSClient(host=databroker_host, port=databroker_port)
client.connect()
value_to_send = 1

def log(msg):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{now} {msg}", file=sys.stderr, flush=True)

try:
    while True:
          movement = ""
          x_value = x_channel.value
          y_value = y_channel.value

          if x_value - 13180 > 20:
            print("right")
            movement = "right"
            client.set_current_values({joy_name_right: Datapoint(value_to_send)})
          else:
             client.set_current_values({joy_name_right: Datapoint(0)})

          if 13180 - x_value > 20:
            print("left")
            movement = "left"
            client.set_current_values({joy_name_left: Datapoint(value_to_send)})
          else:
            client.set_current_values({joy_name_left: Datapoint(0)})

          if y_value - 13044 > 20:
            print("jump")
            movement = "jump"
            client.set_current_values({joy_name_up: Datapoint(value_to_send)})
          else:
            client.set_current_values({joy_name_up: Datapoint(0)})


          print(f"X: {x_value}, Y: {y_value}")
          time.sleep(0.1)
except KeyboardInterrupt:
    print("Program interrupted by user")

