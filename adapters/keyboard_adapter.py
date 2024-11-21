from kuksa_client.grpc import VSSClient
import subprocess
import time
from adapters.parameters import signal_name_left, signal_name_right, signal_name_up


KEY_REPEAT = 15

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
    Lateral = client.get_current_values([signal_name_right])
    Longitudinal = client.get_current_values([signal_name_left])
    Vertical = client.get_current_values([signal_name_up])

    if Lateral[signal_name_right].value > 0.0:
        subprocess.run(str_right, shell=True)

    if Longitudinal[signal_name_left].value > 0.0:
        subprocess.run(str_left, shell=True)

    if Vertical[signal_name_up].value > 0.0:
        subprocess.run(str_up, shell=True)

    time.sleep(0.0001)


