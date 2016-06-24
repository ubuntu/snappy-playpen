# Intellij Idea CE snap

This project creates a working snap of Intellij Idea Community Edition.

To get this done, we need to do the following:
 - edit the ant plugin
 - build from current git
 - extract created tarfile

## Current state

Working features:
 - ide

Known issues:
  - missing theme
  - uses gtk-launch, should actually only need a launcher for the fonts

TODO:
 - replace gtk-launch with launcher
 - fix theme
 
