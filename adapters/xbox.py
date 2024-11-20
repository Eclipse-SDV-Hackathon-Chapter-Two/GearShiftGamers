import pygame
from kuksa_client.grpc import Datapoint
from kuksa_client.grpc import VSSClient

databroker_host = 'localhost'
databroker_port = '55555'
joystick_tolerance = 20
value_to_send = 1


class XboxController(object):

    client = VSSClient(host=databroker_host, port=databroker_port)
    joystick = None

    def __init__(self):
        pygame.joystick.init()
        self.joystick = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())][0]
        self.client.connect()

    def main(self):
        # main loop
        while True:
            # read the xbox controller inputs and translate them to the data broker

            # left
            if self.joystick.get_axis(axis_number=0) < -joystick_tolerance:
                self.client.set_current_values({'Acceleration.Longitudinal': Datapoint(value_to_send)})

            # right
            if self.joystick.get_axis(axis_number=0) > joystick_tolerance:
                self.client.set_current_values({'Acceleration.Lateral': Datapoint(value_to_send)})

            # up
            if self.joystick.get_axis(axis_number=1) > joystick_tolerance:
                self.client.set_current_values({'Acceleration.Vertical': Datapoint(value_to_send)})
