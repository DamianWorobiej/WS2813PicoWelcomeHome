# About the project

Here's very simple program that lights WS2813 LED strip with Raspberry Pi Pico.

## Things I know you want to ask

Don't worry, I'm psycho, not psychic, that's just a guesswork on my part.

### Why?

I have a fairly long hallway. Overhead lights are located roughly in the middle of it, which means it's very dark near the entrance door. It was kinda hard to get my shoes on when I didn't see them, so I figured I can get tiny brain to fix that issue.

### No, but why would you use addressable RGB strip to do that, wouldn't regular strip be enough?

Oh, right. That's the one I could get my hands on that wasn't bilion meters long. 1 meter was just what I needed.

### Why wouldn't you get some ready product that would do exactly the same thing?

Where's the fun in that? Also why don't you mind your own business while we're at it? You're here for code, aren't you?

# Setup

This might not be surprise to anybody but me, but setting everything up took 95% of the time required to do this. Let's have me go through this trauma so you don't have to.

## MicroPython vs C/C++

I started this project wanting to do it in C/C++, because those are languages Cool Guys use and they don't have some  "micro" in their name. That changed because I couldn't find any reasonable library that would prevent me from spending two weeks on it. Plus compiling, disconnecting Pi, connecting it back while pressing the button and putting the binary into the board is tedious, ain't nobody got time for that.

Also, did you know MicroPython is a language Cool Guys use and is using more than one letter of alphabet in their name?

## IDE

I would love to use VS Code, but I'm lazy and couldn't find any out-of-the box solutions, so I ended up using Thonny. It's really neat to just plug the board in and work with it without any hoops.

I followed [this amazing guide](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/0) that will guide you through Thonny's setup, how to use it, getting Python on your board and some other basic stuff.

## Packages
- grove_py
- pico_zero
- smbus2

# Connecting cables

# Few words about code

https://www.youtube.com/watch?v=TTsP35xeigA

# Potential next steps

- Battery powah. Plug-free is stress-free
- Power switch, obviously
- Low battery notification. Let's be surprised by lack of milk, not lack of juice.