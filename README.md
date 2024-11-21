# Project overview

Welcome to GearShiftGamer Hackathon project.
This overview includes everything you need 
to know about this project along with links 
to important resources and people.

## Project description

The implementation of the Play-by-wire hackathon challenge
https://github.com/Eclipse-SDV-Hackathon-Chapter-Two/challenge-play-by-wire

## Goals

1. Define the inputs
    - Player 1 uses the Xbox gamepad
    - Player 2 uses an in-car joystick, simulated by
2. Choose a game
    - Blobby Volley 2
        - https://sourceforge.net/projects/blobby/
        - C++ source code
3. Develop the solution architecture
    - [Diagram](solution_architecture.drawio.svg)
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
3. [Game Valley Blobby 2](https://sourceforge.net/projects/blobby/)
    1. Dependencies `sudo apt-get install build-essential libsdl2-dev libphysfs-dev libboost-all-dev`
4. [Ankaios](https://eclipse-ankaios.github.io/ankaios/latest/)
5. [Ankaios Dashboard](https://github.com/FelixMoelders/ankaios-dashboard/)
6. [Kuksa](https://eclipse-kuksa.github.io/kuksa-website/)
7. [Podman](https://phoenixnap.com/kb/podman-tutorial)

## Tool stack

* Linux OS (host OS for both Raspberry Pi's and laptop)
* C++ (game source code)
* Python 3 (adapter implementation)
* Podman (containerizing of components)
* Ankaios (orchestrating of the containers)
* Kuksa (standard implementations of certain modules)
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

## Showcase/Presentation

1. Set the stage
2. Present the business case
3. Start all modules
4. Use both input interfaces to play the game
5. Give an outlook to perspectives

## Architecture

![Solution architecture](solution_architecture.drawio.svg)
