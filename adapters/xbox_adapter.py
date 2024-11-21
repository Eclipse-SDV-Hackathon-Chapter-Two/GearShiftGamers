# https://www.pygame.org/docs/ref/joystick.html#pygame.joystick.Joystick.get_axis
import pygame
from kuksa_client.grpc import Datapoint
from kuksa_client.grpc import VSSClient
import time
import random
from adapters.parameters import SIGNAL_NAME_LEFT, SIGNAL_NAME_RIGHT, SIGNAL_NAME_UP, DATABROKER_HOST, DATABROKER_PORT

joystick_tolerance = 0.2
value_to_send = 1


class XboxController(object):

    joystick = None

    def __init__(self):
        # Initialize Pygame
        pygame.init()
        pygame.joystick.init()

        # Initialize Joystick
        self.joystick = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())][0]
        self.joystick.init()

        self.client = None

    def connect_to_databroker(self) -> None: 
        self.client = VSSClient(host=DATABROKER_HOST, port=DATABROKER_PORT)
        self.client.connect()


    def main(self) -> None:
        
        while True:
            time.sleep(0.01)
            pygame.event.pump()

            try:
                if self.client is None:
                    self.connect_to_databroker()
                    print("connected to databroker")

                axis_0 = self.joystick.get_axis(0)
                axis_1 = self.joystick.get_axis(1)
                rand_offset = random.uniform(0.0, 0.1)

                # left
                if axis_0 < -joystick_tolerance:
                    self.client.set_current_values({SIGNAL_NAME_LEFT: Datapoint(value_to_send + rand_offset)})
                    print("<-")
                else:
                    self.client.set_current_values({SIGNAL_NAME_LEFT: Datapoint(0)})

                # right
                if axis_0 > joystick_tolerance:
                    self.client.set_current_values({SIGNAL_NAME_RIGHT: Datapoint(value_to_send + rand_offset)})
                    print("->")
                else:
                    self.client.set_current_values({SIGNAL_NAME_RIGHT: Datapoint(0)})

                # up
                if axis_1 < -joystick_tolerance:
                    self.client.set_current_values({SIGNAL_NAME_UP: Datapoint(value_to_send + rand_offset) })
                    print("^")
                else:
                    self.client.set_current_values({SIGNAL_NAME_UP: Datapoint(0)})

            except Exception as e:
                print("Kuksa Databroker is down...try to connect")
                self.client = None
                time.sleep(1)

if __name__=="__main__":
    xbox = XboxController()
    xbox.main()