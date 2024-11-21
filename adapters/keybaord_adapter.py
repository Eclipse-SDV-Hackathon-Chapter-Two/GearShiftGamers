from kuksa_client.grpc import Datapoint
from kuksa_client.grpc import DataEntry
from kuksa_client.grpc import DataType
from kuksa_client.grpc import EntryUpdate
from kuksa_client.grpc import Field
from kuksa_client.grpc import Metadata
from kuksa_client.grpc import VSSClient
import subprocess
import time

KEY_REPEATR = 15

# databroker_host = '127.0.0.1'
databroker_host = '0.0.0.0'
databroker_port = '55555'
client = VSSClient(databroker_host, databroker_port)
client.connect()


str_right = "xdotool key D && xdotool key D \n"
str_left = "xdotool key A && xdotool key A \n"
str_up = "xdotool key W && xdotool key W \n"

process = subprocess.Popen(["/bin/bash"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)



while True:
    Lateral = client.get_current_values(['Vehicle.Acceleration.Lateral'])
    Longitudinal = client.get_current_values(['Vehicle.Acceleration.Longitudinal'])
    Vertical = client.get_current_values(['Vehicle.Acceleration.Vertical'])




    if Lateral["Vehicle.Acceleration.Lateral"].value > 0.0:
        subprocess.run(str_right, shell=True)




    if Longitudinal["Vehicle.Acceleration.Longitudinal"].value > 0.0:

        subprocess.run(str_left, shell=True)

    if Vertical["Vehicle.Acceleration.Vertical"].value > 0.0:

        subprocess.run(str_up, shell=True)


    # print(current_values)
    time.sleep(0.0001)


