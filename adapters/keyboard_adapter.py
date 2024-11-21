from kuksa_client.grpc import VSSClient
import subprocess
import time
from datetime import datetime, timedelta
from xdo import Xdo
import pexpect

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

str_right = f'xdotool key --delay 1 {30*'D '} D'
str_left = f'xdotool type --delay 1 "{30*'A'}"'
str_up = f'xdotool type --delay 1 "{3*'W'}"'

# str_left = "xdotool key A && xdotool key A \n"
# str_up = "xdotool key W && xdotool key W \n"

arrow_right = "xdotool key Right && xdotool key Right && xdotool key Right\n"
arrow_left = "xdotool key Left && xdotool key Left && xdotool key Left\n"
arrow_up = "xdotool key Up && xdotool key Up && xdotool key Up\n"

process = subprocess.Popen(["/bin/bash"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

stopwatch = time.time()

start_time = datetime.min
xbox_ri_Last = start_time
xbox_le_Last = start_time
xbox_up_Last = start_time
joy_ri_Last = start_time
joy_le_Last = start_time
joy_up_Last = start_time

# Open a new bash session
child = pexpect.spawn('bash')

while True:

    # get_value = client.subscribe_current_values
    get_value = client.get_current_values
    # get_value = client.subscribe

    # print("stopwatch:", time.time() - time.time())
    xbox_ri = get_value([signal_name_right])[signal_name_right]
    # xbox_ri = get_value([signal_name_right])
    # for i in xbox_ri:
        # print(i)
    xbox_le = get_value([signal_name_left])[signal_name_left]
    xbox_up = get_value([signal_name_up])[signal_name_up]

    joy_ri = get_value([joy_name_right])[joy_name_right]
    joy_le = get_value([joy_name_left])[joy_name_left]
    joy_up = get_value([joy_name_up])[joy_name_up]



    try:
        print("joy: ", joy_ri.value, joy_le.value, joy_up.value)

        if joy_ri.value > 0.1:
            pass
            subprocess.run(arrow_right, shell=True)


        if joy_le.value > 0.1:
            pass
            subprocess.run(arrow_left, shell=True)

        if joy_up.value > 0.1:
            pass
            subprocess.run(arrow_up, shell=True)
    except:
        print("start joystick of pi@vehicle")


    try:
        print("xbox:", xbox_ri.value, xbox_le.value, xbox_up.value)
        # print("xbox:", xbox_ri.timestamp, xbox_le.timestamp, xbox_up.timestamp)

        if xbox_ri.value > 0.1 and xbox_ri.timestamp > xbox_ri_Last:
            pass
            # subprocess.run(str_right, shell=True)
            # xdo.focus_window(0, "d", 0)
            child.sendline(str_right)
            # child.interact()

        if xbox_le.value > 0.1 and xbox_le.timestamp > xbox_le_Last:
            pass
            # subprocess.run(str_left, shell=True)
            child.sendline(str_left)

        if xbox_up.value > 0.1 and xbox_up.timestamp > xbox_up_Last:
            pass
            subprocess.run(str_up, shell=True)
            child.sendline(str_up)

        xbox_ri_Last = xbox_ri.timestamp
        xbox_le_Last = xbox_le.timestamp
        xbox_up_Last = xbox_up.timestamp

    except:
        pass
        print("start xbox controller")

    # time.sleep(0.01)


