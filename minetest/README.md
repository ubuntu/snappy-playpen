# Minetest snap

This project creates a working snap of Mintest from upstream git.

To get this done, we need to do the following:
 - build from current tip of git
 - Add in the default minecraft_game
 - At runtime we copy the default config to a writable area if one doesn't already exist

## Current state

Working features:
 - Minetest as a client to Minetest servers
