# $PROJECT snap

This project will someday build a working snap of `nginx` webserver.

To get this done, we need to do the following:
 - First get `snapcraft` able to find the executable.

## Current state

Working features:
 - Compiles the slightly non-standard approach to build directory structure and
  `./configure` script, from mercurial repo.

Known issues:
  - Doesn't completely snap yet

TODO:
 - Jiggle `snapcraft` until it can find and execute `nginx` on the $SNAP path
