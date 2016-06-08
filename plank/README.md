# plank snap

This project creates a working snap of plank

To get this done, we need to do the following:
 - add custom launcher
 - build from current git
 - install using --devmode

## Current state

Working features:
 - Launches and displays list of apps/windows
 - Shows names and icons for apps installed via Click
 - App switching/minimizing when clicked
 - Quick Lists
 - App open detection

Known issues:
  - Icons of apps installed with apt-get do not show
  - Names of apps installed with apt-get do not show
  - Keep in Dock doesn't work for apt-get installed apps

TODO:
 - Track down the cause of missing apt-get app meta-data
 
