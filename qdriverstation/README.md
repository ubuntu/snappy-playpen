# QDriverStation

This project creates a working snap of the [QDriverStation](https://github.com/WinT-3794/QDriverStation), directly from its Git repository. 

## About the project

The QDriverStation is an cross-platform and open-source alternative to the FRC Driver Station. It allows operation of (but not limited to) FRC robots. For the moment, FRC 2009-2014 and FRC 2015-2016 communication protocols are supported. 

## Current state

Working features:

- The application itself is compiled, installed and executed successfully

Known issues:

- Audio & joystick input does not work. This is a problem with snappy, not with this project.
- This project uses *QProcess* to get CPU & Battery information. However, we cannot do that due to the snappy "sandbox" (AFAIK)
