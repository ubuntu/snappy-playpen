# tyrant-unleashed-optimizer snap

This project creates a working snap of tyrant-unleashed-optimizer (tuo)

To get this done, we need to do the following:
 - build from current git

One can see this as easy example for:
 - multiple commands in one snap (with different plugs for isolation)
 - to use a custom plugin to fixup shortcomings in build systems

## Current state

Working features:
 - updating local card database
 - simulating fights

Known issues:
  - the home plug needs to be connected manually after snap install with
    "sudo snap connect tyrant-unleashed-optimizer:home ubuntu-core:home"
  - you can run all inside /tmp without connecting

Invocation-Card-Update:
  - Note: if you don't have a "data" dir yet you have to create one via ``mkdir data``
  - tyrant-unleashed-optimizer.updatexml

Invocation-SIM:
  - Note: as usual with tuo you have to run this where you have your data/ dir.
  - tyrant-unleashed-optimizer.sim "Lord Silus, Extreme Barrager #2" "Lord Silus, Atomic Wardriver #2" sim 100

TODO:
 -
