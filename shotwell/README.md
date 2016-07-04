# Shotwell snap

This project creates a working snap of Shotwell from gnome git.

To get this done, we need to do the following:
 - build from current git (latest tag)

## Current state

Working features:
 - Photo import from folder

Known issues:
  - Only builds with --no-parallel-build (fixed in master)
  - Starts with gtkconf if installed via --devmode

TODO:
  - Fix the need for --devmode
  - check gtkconf
