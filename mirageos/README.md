# MirageOS snap

This is a ocaml project for creating unikernels.
There is no deb package. It's interesting because it uses a language and a
package manager I haven't used in snapcraft before.

## Current state

Working features:
 - The snap builds and runs in devmode.

To do:
 - More testing to check if all the features are working.
 - Find the missing permissions to remove devmode.

Known issues:
 - The required packages are defined in the source branch, in the mirage.opam
   file. There must be a way to install from this file, instead of redefining
   the dependencies, install them and call make. If we find how to do this,
   the plugin can be upstreamed to snapcraft.
