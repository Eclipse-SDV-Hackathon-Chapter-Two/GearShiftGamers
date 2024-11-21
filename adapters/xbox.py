# https://www.pygame.org/docs/ref/joystick.html#pygame.joystick.Joystick.get_axis
import pygame
from kuksa_client.grpc import Datapoint
from kuksa_client.grpc import VSSClient
import time

# databroker_host = '127.0.0.1'
databroker_host = '0.0.0.0'
databroker_port = '55555'
joystick_tolerance = 0.6
value_to_send = 1


class XboxController(object):

    joystick = None

    def __init__(self):
        # Initialize Pygame
        pygame.init()

        pygame.joystick.init()

        self.joystick = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())][0]
        self.joystick.init()

        self.client = VSSClient(host=databroker_host, port=databroker_port)
        self.client.connect()

    def main(self):
        # main loop
        while True:
            time.sleep(0.01)

            pygame.event.pump()

            # left
            if self.joystick.get_axis(0) < -joystick_tolerance:
                self.client.set_current_values({'Vehicle.Acceleration.Longitudinal': Datapoint(value_to_send)})
                print("left")
            else:
                self.client.set_current_values({'Vehicle.Acceleration.Longitudinal': Datapoint(0)})
                
                
            # right
            if self.joystick.get_axis(0) > joystick_tolerance:
                self.client.set_current_values({'Vehicle.Acceleration.Lateral': Datapoint(value_to_send)})
                print("right")
            else:
                self.client.set_current_values({'Vehicle.Acceleration.Lateral': Datapoint(0)})


            # up
            if self.joystick.get_axis(1) < -joystick_tolerance:
                self.client.set_current_values({'Vehicle.Acceleration.Vertical': Datapoint(value_to_send)})
                print("up")
            else:
                self.client.set_current_values({'Vehicle.Acceleration.Vertical': Datapoint(0)})

            print("")


if __name__=="__main__":
    xbox = XboxController()
    xbox.main()