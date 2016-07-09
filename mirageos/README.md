# MirageOS snap

This is a ocaml project for creating unikernels.
There is no deb package, and it's interesting because it's a new language and
package manager.

## Current state

Working features:
 - The snap builds.
 - The binary on prime/bin/mirage works.

Known issues:
 - Even on devmode, when executing mirageos.mirage, it fails with:
   /bin/sh: 1: /usr/bin/tput: Permission denied
   /bin/sh: 1: /bin/stty: Permission denied
   Fatal error: exception (Sys_error ".: Permission denied")
 - The required packages are defined in the source branch, in the mirage.opam
   file. There must be a way to install from this file, instead of redefining
   the dependencies, install them and call make. If we find how to do this,
   the plugin can be upstreamed to snapcraft.
