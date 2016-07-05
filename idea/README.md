# Intellij Idea CE snap

This project creates a working snap of Intellij Idea Community Edition.

To get this done, we need to do the following:
 - edit the ant plugin
 - build from current git
 - extract created tarfile
 - use custom launcher

## Current state

Working features:
 - ide

Known issues:
  - only starts if installed with --devmode

TODO:
 - fix theme
 
If installed without "--devmode" it returns the following error:
Invalid Log Path: Log path '/home/user/.IdeaIC2016/system/log' is inaccessible.
