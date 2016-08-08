# Cuberite snap

This project creates a working snap of Cuberite from upstream git.

To get this done, we need to do the following:
 - build from current tip of git.
 - stage the Server directory from the source tree.
 - Add a wrapper to copy runtime files to a writable directory and launch the
   server from there.

## Current state

Working features:
 - Game tested with Minecraft 1.9 client.
 - Web Admin.
 - Plugins.

Known issues:
  - Still needs devmode thanks to a call to fchown in the statically-linked
    sqlite3.

TODO:
 - Since Cuberite uses the current working directory for its data, it'd be
   great to be able to manage several instances easily.
 
