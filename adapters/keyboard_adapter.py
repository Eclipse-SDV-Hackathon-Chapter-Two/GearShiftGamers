from kuksa_client.grpc import VSSClient
import subprocess
import time
from datetime import datetime
import pexpect
from adapters.parameters import SIGNAL_NAME_LEFT, SIGNAL_NAME_RIGHT, SIGNAL_NAME_UP, DATABROKER_HOST, \
    DATABROKER_PORT
from adapters.parameters import JOY_NAME_LEFT, JOY_NAME_RIGHT, JOY_NAME_UP

KEY_REPEAT = 15

client = VSSClient(DATABROKER_HOST, DATABROKER_PORT)
client.connect()

str_right = f'xdotool key --delay 1 {30*'D '} D'
str_left = f'xdotool type --delay 1 "{30*'A'}"'
str_up = f'xdotool type --delay 1 "{3*'W'}"'

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

    get_value = client.get_current_values

    xbox_ri = get_value([SIGNAL_NAME_RIGHT])[SIGNAL_NAME_RIGHT]
    xbox_le = get_value([SIGNAL_NAME_LEFT])[SIGNAL_NAME_LEFT]
    xbox_up = get_value([SIGNAL_NAME_UP])[SIGNAL_NAME_UP]

    joy_ri = get_value([JOY_NAME_RIGHT])[JOY_NAME_RIGHT]
    joy_le = get_value([JOY_NAME_LEFT])[JOY_NAME_LEFT]
    joy_up = get_value([JOY_NAME_UP])[JOY_NAME_UP]

    try:
        print("joy: ", joy_ri.value, joy_le.value, joy_up.value)

        if joy_ri.value > 0.1:
            pass
            child.sendline(arrow_right)

        if joy_le.value > 0.1:
            pass
            child.sendline(arrow_left)

        if joy_up.value > 0.1:
            pass
            child.sendline(arrow_up)
    except:
        print("start joystick of pi@vehicle")

    try:
        if xbox_ri.value > 0.1 and xbox_ri.timestamp > xbox_ri_Last:
            pass
            child.sendline(str_right)

        if xbox_le.value > 0.1 and xbox_le.timestamp > xbox_le_Last:
            child.sendline(str_left)

        if xbox_up.value > 0.1 and xbox_up.timestamp > xbox_up_Last:
            pass
            child.sendline(str_up)

        xbox_ri_Last = xbox_ri.timestamp
        xbox_le_Last = xbox_le.timestamp
        xbox_up_Last = xbox_up.timestamp

    except:
        pass
        print("start xbox controller")
