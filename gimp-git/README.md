# GIMP-from-git snap

This project is a work in progress to build GIMP (and its dependencies)
from the git repositories.

## Current State

Not even 100% certain about the dependencies yet, probably some extra and
perhaps some missing. There are definite environment variables which need
to be integrated into the `snapcraft.yaml` build file (see `env.sh` and
`env2.sh`), notably the explicit GIO library link, ACLOCAL flags, and PKG
CONFIG PATH. Configuring the build process so that `staged parts` become
dependencies for the later `parts` with correct library links.

---

Having built GIMP before successfully from source, using information from
several places, and being very interested in the future of Ubuntu I wanted
to try out snapcrafting. Because there are several `parts` to build, which
are order sensitive, and having a large number of dependencies, which
requires some environment configuration, this is not something I expect to
do without some help. However, I really want to show enthusiasm for the
new package format and the Ubuntu project, the marquee applications in the
FLOSS ecosystem should be built as `snap` packages as soon as possible.
