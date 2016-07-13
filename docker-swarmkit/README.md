# Docker swarmkit snap

This is a go project for orchestrating distributed systems, not yet relased.

## Current state

Working features:
 - The snap builds and executes in devmode.

Known issues:
 - A windows dependency tries to build in linux: https://github.com/docker/swarmkit/issues/1067
   Because of that, we need a patched version of the go plugin.
