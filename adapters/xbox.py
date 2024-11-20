import pygame
import random
from kuksa_client.grpc import Datapoint
from kuksa_client.grpc import DataEntry
from kuksa_client.grpc import DataType
from kuksa_client.grpc import EntryUpdate
from kuksa_client.grpc import Field
from kuksa_client.grpc import Metadata
from kuksa_client.grpc import VSSClient

databroker_host = 'localhost'
databroker_port = '55555'

pygame.init()


# kuksa databroker
client = VSSClient(databroker_host, databroker_port)
client.connect()

# main loop
while True:
    # get brake signal to move the right player up
    current_values = client.get_current_values(
        ['Acceleration.Longitudinal', 'Vehicle.Chassis.Accelerator.PedalPosition'])
    if current_values['Acceleration.Longitudinal'] is not None:
        if current_values['Acceleration.Longitudinal'].value > 0:
            right_paddle_vel = -0.9
            second_right_paddle_vel = -0.9
        elif current_values['Vehicle.Chassis.Accelerator.PedalPosition'].value > 20:
            right_paddle_vel = 0.9
            second_right_paddle_vel = 0.9
        else:
            right_paddle_vel = 0
            second_right_paddle_vel = 0