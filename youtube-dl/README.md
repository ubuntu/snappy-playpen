# youtube-dl snap

This project creates a working snap of youtube-dl.

To get this done, we need to do the following:
 - build from current git

## Current state

Working features:
 - video downloading

Known issues:
  - the home plug needs to be connected manually after snap install with 
    "sudo snap connect youtube-dl:home ubuntu-core:home"
  - ffprobe is not found when using `-x --audioformat mp3` option. Fix proposed in pull request

TODO:
 -
 
