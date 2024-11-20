# GearShiftGamers

Project overviewWelcome to Gamer. This canvas includes everything you need to know about this project along with links to important resources and people.

## Project description

The implementation of the Play-by-wire hackathon challenge
https://github.com/Eclipse-SDV-Hackathon-Chapter-Two/challenge-play-by-wire

## Goals

1. Define the inputs
    1. We use a smart device connected to local server as a controller
    2. the API is to define
2. Choose a game
    1. Two alternatives
        1. Blobby Volley
            1. https://github.com/aikikode/pyvolley
                1. python 2.7
            2. https://sourceforge.net/projects/blobby/
        2. https://grantjenks.com/docs/freegames/connect.html
        3. https://sourceforge.net/projects/blobby/
            1. C source code



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

1. SDV hackathon repository https://github.com/Eclipse-SDV-Hackathon-Chapter-Two/GearShiftGamers.git
2. SDV products https://projects.eclipse.org/working-group/eclipse-software-defined-vehicle
3. Game https://sourceforge.net/projects/blobby/
    1. Dependencies `sudo apt-get install build-essential libsdl2-dev libphysfs-dev libboost-all-dev`
        1. cmake: `sudo apt install build-essential`
        2. SDL: `sudo apt-get install libsdl2-dev`
        3. PhysFS: `sudo apt-get install libphysfs-dev`
        4. Boost: `sudo apt-get install libboost-all-dev`
4. Ankaios https://eclipse-ankaios.github.io/ankaios/latest/

## Tool stack

* Linux OS
* C++

## Hardware Setup

* Controller
* Display
* Gamepad
* Mobile Device (Smartphone)
* WLAN
    * SSID `bierkiste`
    * password `AkWyapCidjuOckakkorfObAr`
* Raspberry Pi 
    * ip address: `192.168.0.148`
    * user: `pi`
    * password: `raspberry`

## Showcase/Presentation

1. Compile common known Game (BlobbyVolley) for HPC (Rasp4)
2. Deploy game via MUTO on the HPC (GameStore)
3. (Start the game (Ankaios)?)
4. Use several input interfaces to play (Data Broker Ankaios) the game

