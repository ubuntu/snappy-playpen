# Docker Distribution snap

This is a go project to register and distribute docker images.

## Current state

Working features:
 - The snap builds and executes. More testing is required to verify all the functions.

To do:
 - Figure out the interfaces required to remove devmode.

Known issues:
 - The snap uses a custom plugin that's a mix between the make and the go plugins.
