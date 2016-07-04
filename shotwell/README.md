# Shotwell snap

This project creates a working snap of Shotwell from gnome git.

To get this done, we need to do the following:
 - build from current git

## Current state

Working features:
 - Photo import from folder

Known issues:
  - Only builds with --no-parallel-build
  - Does not start
      - If installed without --devmode the program quits with:
          sh: 0: getcwd() failed: No such file or directory
          sh: 0: getcwd() failed: No such file or directory
          shell-init: error retrieving current directory: getcwd: cannot access parent directories: No such file or directory
      - If installed with --devmode the program looks for the resources (icons) in the snappy-playpen folder instead of $SNAP
TODO:
  - Fix the need for --devmode
 
