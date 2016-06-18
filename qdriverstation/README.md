# QDriverStation

This project creates a working snap of the [QDriverStation](https://github.com/WinT-3794/QDriverStation).

The QDriverStation is an cross-platform and open-source alternative to the FRC Driver Station. It allows operation of (but not limited to) FRC robots.

To get this done, we need to do the following:
 - add custom launcher
 - build from current git

## Current state

Working features:

- The application itself is compiled, installed and executed successfully

Known issues:

- Audio & joystick input does not work. This is a problem with snappy, not with this project.
- This project uses *QProcess* to get CPU & Battery information. However, we cannot do that due to the snappy "sandbox" (AFAIK)
