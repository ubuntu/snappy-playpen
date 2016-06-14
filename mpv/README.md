# mpv snap

This project creates a working snap of mpv from a snapshot of upstream git.

To get this done, we need to do the following:
 - build upstream ffmpeg
 - grab the 'waf' build tool which matches this mpv snapshot
 - build from current mpv snapshot using waf

## Current state

Working features:
 - video playback

Known issues:
  - Must be installed with --devmode
