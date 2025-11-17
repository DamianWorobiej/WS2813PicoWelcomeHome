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

### *On second thought...*

I actually managed to get it to work. I flashed micropython, did some random clicks like initialize micopico project or something and bada bing bada boom I can plug my microcontroller, directly point the right COM port in the settings and stuff just works. Great success!

## Packages

See requirements-dev.txt file

# Connecting cables

# Few words about code

## "I see a lot of files there for such a simple project, what's up with that?"

I like to abstract stuff a lot. Plus I've got a couple of other projects I will likely ~~steal~~ borrow some modules for (battery level control being the most likely one).

## "Why there are two implementations for led stips?"

That one is strange, not gonna lie.

During development I figured I will do my best to use some library for controlling the strip. Ultimately there **must** have been some lib for that, right?

There was but something was off. Everything was good and dandy with my mighty WS2813 strip when I had my controller connected to my PC, but as soon as I switched to powering pico from outside weird things started to happen. For the life of me I couldn't control first diode on the strip, it was bright red no matter what. Everything besides that was ok, but I just couldn't have that on my "end product".

Ultimately [this video](https://www.youtube.com/watch?v=TTsP35xeigA) was my saving grace. I don't pretend to understand fully what's going on besides that there is some assembly, but it works and that's all I needed.

The issue might have been with pico using 3.3V output for GPIOs while strip operates on 5V and using logic level shifter would solve this, but I've got it to work now and if something stops working it's Future Me's problem, not mine. Screw that guy.

# Potential next steps

- Battery powah. Plug-free is stress-free
- Power switch, obviously
- 3D printed case
- deep sleep. There's no reason to run the loop constantly with such low usage
- log saving