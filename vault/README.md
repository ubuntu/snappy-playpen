# vault snap

This project creates a working snap of hashicorp's vault.
This is a CLI go project for handling secrets. So the way go handles
dependencies and the fact that it's a security tool that needs to be always
up-to-date make it a nice use case for snappy.

## Current state

Working features:
 - everything

Known issues:
 - the project had to be added to the snapcraft.yaml as a go-package instead
   of as source. Reported in https://bugs.launchpad.net/snapcraft/+bug/1583426
