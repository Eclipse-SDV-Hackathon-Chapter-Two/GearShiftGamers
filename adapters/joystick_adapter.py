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
from parameters import JOY_NAME_LEFT, JOY_NAME_RIGHT, JOY_NAME_UP, DATABROKER_HOST, DATABROKER_PORT

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
x_channel = AnalogIn(ads, ADS.P0)
y_channel = AnalogIn(ads, ADS.P1)

client = VSSClient(host=DATABROKER_HOST, port=DATABROKER_PORT)
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
            client.set_current_values({JOY_NAME_RIGHT: Datapoint(value_to_send)})
        else:
            client.set_current_values({JOY_NAME_RIGHT: Datapoint(0)})

        if 13180 - x_value > 20:
            print("left")
            movement = "left"
            client.set_current_values({JOY_NAME_LEFT: Datapoint(value_to_send)})
        else:
            client.set_current_values({JOY_NAME_LEFT: Datapoint(0)})

        if y_value - 13044 > 20:
            print("jump")
            movement = "jump"
            client.set_current_values({JOY_NAME_UP: Datapoint(value_to_send)})
        else:
            client.set_current_values({JOY_NAME_UP: Datapoint(0)})

        print(f"X: {x_value}, Y: {y_value}")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program interrupted by user")

