# Shotwell snap

This project creates a working snap of Shotwell from gnome git.

To get this done, we need to do the following:
 - build from current git

## Current state

Working features:
 - Photo import from folder

Known issues:
  - Only starts if installed with --devmode.
    If installed without --devmode the program quits with:
    /snap/shotwell/x1/bin/gtk-launch: line 111: 142916 Bad system call         cp -a $SNAP/usr/share/mime $XDG_DATA_HOME

TODO:
  - Fix the need for --devmode
 
