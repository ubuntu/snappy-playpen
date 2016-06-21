# ffmpeg snap

This project creates a working snap of `ffmpeg`.

To get this done, we need to do the following:
 - build from current git

## Current state

Working features:
 - `ffmpeg`, accessed through `ffmpeg.convert` once installed.

Known issues:
  - Other command line tools (`ffmplay`, `ffserver`, `ffprobe`) do not
    build yet.
