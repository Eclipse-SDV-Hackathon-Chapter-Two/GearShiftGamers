# Project overview

Welcome to GearShiftGamer Hackathon project.
This overview includes everything you need 
to know about this project along with links 
to important resources and people.

## Project description

The implementation of the Play-by-wire hackathon challenge
https://github.com/Eclipse-SDV-Hackathon-Chapter-Two/challenge-play-by-wire

## Our goals

- work with the Eclipse SDV ecosystem
- learn new stuff
- networking
- having fun

## Steps

1. Define the inputs
    - Player 1 uses the Xbox gamepad
    - Player 2 uses an in-car joystick, simulated by a Raspberry Pi
2. Choose a game
    - Blobby Volley 2
        - https://sourceforge.net/projects/blobby/
        - C++ source code
3. Develop the solution architecture
    - [Diagram](assets/solution_architecture.drawio.svg)
4. Define the interfaces
5. Implement the necessary modules, test it
6. Create the pitch slides

## Team

| Role        | Name             |
|-------------|------------------|
| Team member | Lukas Langer     |
| Team member | Muzi Xu          |
| Team member | Sebastian Probst |
| Team member | Ilja Stasewitsch |
| Team member | Pavel Spakowski  |

## Task tracker

We use this task tracker to keep track of team tasks:
https://app.slack.com/lists/T02MS1M89UH/F081NGQ3UPL

## Key resources

1. [SDV hackathon repository](https://github.com/Eclipse-SDV-Hackathon-Chapter-Two/GearShiftGamers.git)
2. [SDV product list](https://projects.eclipse.org/working-group/eclipse-software-defined-vehicle)
3. [Game Blobby Volley 2](https://sourceforge.net/projects/blobby/)
    1. Dependencies `sudo apt-get install build-essential libsdl2-dev libphysfs-dev libboost-all-dev`
4. [Ankaios](https://eclipse-ankaios.github.io/ankaios/latest/)
5. [Ankaios Dashboard](https://github.com/FelixMoelders/ankaios-dashboard/)
6. [Kuksa](https://eclipse-kuksa.github.io/kuksa-website/)
7. [Podman](https://phoenixnap.com/kb/podman-tutorial)
8. [Python](https://www.python.org)
9. [Visual Studio Code](https://code.visualstudio.com)
10. [JetBrains PyCharm](https://www.jetbrains.com/pycharm/)

## Tool stack

* Linux OS (host OS for both Raspberry Pi's and laptop)
* C++ (game source code)
* Python 3 (adapter implementation)
* Podman (containerization of components)
* Ankaios (orchestration of the containers)
* Kuksa (communication between different nodes)
* Visual Studio Code and JetBrains PyCharm

## Hardware Setup

* Xbox Gamepad
* Joystick
* Display
* Local WLAN
* 2x Raspberry Pi as
    * HPC
    * Door ECU
* Linux laptop with x86 processor architecture as
    * Gaming unit
* Dedicated laptop for dashboard showcase

## Showcase/Presentation

1. Set the stage
2. Present the business case
3. Start all modules
4. Use both input interfaces to play the game
5. Give an outlook to perspectives

## Architecture

![Solution architecture](assets/solution_architecture.drawio.svg)

## Important architecture decisions

### Game

For purposes of the Hackathon challenge, a game should be chosen.
The following criteria should be fulfilled:

- multiplayer
- compatible with ARM and/or x86 processor architectures (source code open in the best case)
- support for Linux
- simple controls
- good attraction potential

The game [Valley Blobby 2](https://sourceforge.net/projects/blobby/)
was chosen.

### Transport layer

We use [Kuksa](https://eclipse-kuksa.github.io/kuksa-website/)
gRPC client to transport signals.

### Signal definition

We use some existing signals for transport controls 
from the input devices to the game.

Xbox-Controller:
| Signal name | Purpose |
|-------------------------------------|------------|
| `Vehicle.Acceleration.Longitudinal` | Move left  |
| `Vehicle.Acceleration.Lateral`      | Move right |
| `Vehicle.Acceleration.Vertical`     | Jump       |

Adafruit-Joystick
| Signal name                         | Purpose    |
|-------------------------------------|------------|
| `Vehicle.AngularVelocity.Roll`     | Move left  |
| `Vehicle.AngularVelocity.Pitch`    | Move right |
| `Vehicle.AngularVelocity.Yaw`      | Jump       |


### Containerizing

Every module is set in a Docker container.
The container configuration is set by corresponding .dockerfile.

We use [Podman](https://phoenixnap.com/kb/podman-tutorial)
for creation of and managing the containers.

An [Ankaios](https://eclipse-ankaios.github.io/ankaios/latest/)
instance is used for container orchestration.

### Implementation toolstack

We use [Python 3](https://www.python.org) and IDE's
[Visual Studio Code](https://code.visualstudio.com) and
[JetBrains PyCharm](https://www.jetbrains.com/pycharm/)
for code developing.

### Adaptation signals for game

We simulate keyboard controls for both players.

Player 1 uses the following keys:

| Key | Purpose    |
|-----|------------|
| A   | Move left  |
| D   | Move right |
| W   | Jump       |

Player 2 uses the cursor keys:

| Key | Purpose    |
|-----|------------|
| ←   | Move left  |
| →   | Move right |
| ↑   | Jump       |

We use calls for Linux tool
[xdotool](https://github.com/jordansissel/xdotool)
to fake the keystrokes if corresponding signals
are received.

For simulation of the human key pressing, 
we send every keystroke 30 times with a delay of 1 ms.

````python
str_left = f'xdotool type --delay 1 "{30*'A'}"'
````

## How-to's

### How to install Ankaios

```shell
curl -sfL https://github.com/eclipse-ankaios/ankaios/releases/latest/download/install.sh | bash -
```

### How to configurate Ankaios Server

The content of [Service] /etc/systemd/system/ank-server.service has to be edited as:

````dockerfile
[Service]
Environment="RUST_LOG=info"
ExecStart=/usr/local/bin/ank-server --insecure -a {HOST_IP_ADDRESS:25551} --startip-config /etc/ankaois/state.yaml
````

### How to configurate Ankaios Agent

The content of [Service] /etc/systemd/system/ank-agent.service has to be edited as:

````dockerfile
[Service]
Environment="RUST_LOG=info"
ExecStart=/usr/local/bin/ank-server --insecure -s {HOST_IP_ADDRESS:25551} --name {AGENT_NAME}
````

### How to set agent with YAML file manifest

The content of `/etc/ankaios/state.yaml` has to be edited.

Add databroker manifest in `/etc/ankaios/state.yaml`:

````yaml
apiVersion: v0.1
workloads:
  databroker:
    runtime: podman
    agent: agent_databroker
    runtimeConfig: |
      image: ghcr.io/eclipse/kuksa.val/databroker:0.4.1
      commandArgs: ["--insecure"]
      commandOptions: ["--net=host"]
````

Add joystick manifest in `/etc/ankaios/state.yaml`:

````yaml
apiVersion: v0.1
workloads:
  joystick:
    runtime: podman
    agent: agent_joy
    runtimeConfig: |
      image: joystick_adapter //here you have to replace with your own image path
      commandArgs: ["--insecure"]
      commandOptions: ["--net=host"]
````

### How to start Ankaios Server

Log into the host machine that runs the server.

Activate the server with command:

````shell
sudo systemctl start ank-server
````

### How to start Ankaios Agent

Log into the host machine that runs the agent.
First run

````shell
sudo systemctl start ank-agent
````

And then run

````shell
ank-agent -k -s {HOST_IP_ADDRESS:PORT_NUMBER} -n {AGENT_NAME}
````

## An obligatory Ai-generated team picture

![Team](assets/team.webp)
