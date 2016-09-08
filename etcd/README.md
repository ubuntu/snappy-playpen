# etcd snap

This project creates a working snap of coreos etcd.
This is a popular project, base of many distributed systems.
etcd version on yakkety is 2.2.5, and upstream is now in 3.0.6. So snaps will
be a nice way to deliver faster versions.

It is using a custom plugin based on snapcraft's go plugin. This one sets up
the go paths, and then calls the build command from the etcd repository.

## Current state

Working features:
 - The binaries run in devmode.

To do:
 - More testing is needed to figure out the required interfaces for strict mode.

Known issues:
 - This can't be upstreamed yet because of bug https://bugs.launchpad.net/snapcraft/+bug/1615242
