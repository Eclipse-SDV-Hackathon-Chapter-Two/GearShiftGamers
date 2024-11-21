from kuksa_client.grpc import VSSClient
import subprocess
import time
try:
    from adapters.parameters import signal_name_left, signal_name_right, signal_name_up
    from adapters.parameters import joy_name_left, joy_name_right, joy_name_up
except:
    from parameters import signal_name_left, signal_name_right, signal_name_up
    from parameters import joy_name_left, joy_name_right, joy_name_up

KEY_REPEAT = 15

# databroker_host = '127.0.0.1'
databroker_host = '192.168.0.148'
databroker_port = '55555'
client = VSSClient(databroker_host, databroker_port)
client.connect()

str_right = "xdotool key D && xdotool key D \n"
str_left = "xdotool key A && xdotool key A \n"
str_up = "xdotool key W && xdotool key W \n"

arrow_right = "xdotool key Right && xdotool key Right && xdotool key Right\n"
arrow_left = "xdotool key Left && xdotool key Left && xdotool key Left\n"
arrow_up = "xdotool key Up && xdotool key Up && xdotool key Up\n"

process = subprocess.Popen(["/bin/bash"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

stopwatch = time.time()

while True:
    print("stopwatch:", time.time() - time.time())
    Lateral = client.get_current_values([signal_name_right])
    Longitudinal = client.get_current_values([signal_name_left])
    Vertical = client.get_current_values([signal_name_up])

    Roll = client.get_current_values([joy_name_right])
    Pitch = client.get_current_values([joy_name_left])
    Yaw = client.get_current_values([joy_name_up])

    # print(Pitch)

    try:
        print(Roll[joy_name_right].value, Pitch[joy_name_left].value, Yaw[joy_name_up].value)
        if Roll[joy_name_right].value > 0.0:
            subprocess.run(arrow_right, shell=True)

        if Pitch[joy_name_left].value > 0.0:
            subprocess.run(arrow_left, shell=True)

        if Yaw[joy_name_up].value > 0.0:
            subprocess.run(arrow_up, shell=True)
    except:
        print("start joystick of pi@vehicle")


    try:
        if Lateral[signal_name_right].value > 0.0:
            subprocess.run(str_right, shell=True)

        if Longitudinal[signal_name_left].value > 0.0:
            subprocess.run(str_left, shell=True)

        if Vertical[signal_name_up].value > 0.0:
            subprocess.run(str_up, shell=True)
    except:
        pass
        print("start xbox controller")

    time.sleep(0.0001)


