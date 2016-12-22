# champ snap

This project creates a working snap of champ from a snapshot of upstream git.

champ is 2nd screen player for Plex suite of servers and clients.

To get this done, we need to do the following:
 - build upstream ffmpeg
 - grab the 'waf' build tool which matches this mpv snapshot
 - build from current mpv snapshot using waf
 - build from current champ snapshot using go

## Running

```$ champ -n "Living room"```

## Current state

Working features:
 - all
