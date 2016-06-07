# kdenlive snap

The goal of this project is to create working snap of kdenlive and dependencies.

To do this we:-
 - Grab upstream ffmpeg and build from source
 - Grab upstream kdenlive and build from source
 - Add a qt5-launch wrapper script

## Current state

 - Segfaults (unsolved as yet) or dies
 - Pulseaudio issue resolved in snapcraft 2.0.7
 - udev issue workaround:-
```
sudo nano /var/lib/snapd/apparmor/profiles/snap.kdenlive.kdenlive
```

Paste this around line 20, between the existing {}:-

```
# pulseaudio
/etc/pulse/ r,
/etc/pulse/* r,
/{run,dev}/shm/pulse-shm-* rk,
owner /{,var/}run/user/*/pulse/ r,
owner /{,var/}run/user/*/pulse/native rwk,
# opengl
/run/udev/data/+pci** r,
```

Process the updated apparmor profile

```
sudo apparmor_parser -r /var/lib/snapd/apparmor/profiles/snap.kdenlive.kdenlive
```
