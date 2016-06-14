# GIMP-from-git snap

This project is a work in progress to build GIMP (and its dependencies)
from the git repositories.

- First, everything the devs do is amazing, and they are always right
- Second, following old recipes (particularly for build environments that
  are not _snapcrafting_) is making more work for yourself than starting
  from basics and reading the docs

## Current State

  Getting very close with `snapcraft build`, legitimately all the way
  through to building `gimp` itself, which continues to fail in
  a `cleanbuild` on the `libmypaint >= 1.3.0` and `gegl-0.3 >=0.3.6`
  dependencies. Build breaks much earlier on the host machine, best luck
  in a `$ snapcraft cleanbuild`.

---

Having built GIMP before successfully from source, using information from
several places, and being very interested in the future of Ubuntu I wanted
to try out snapcrafting. Because there are several `parts` to build, which
are order sensitive, and having a large number of dependencies, which
requires some environment configuration, this is not something I expect to
do without some help. However, I really want to show enthusiasm for the
new package format and the Ubuntu project, the marquee applications in the
FLOSS ecosystem should be built as `snap` packages as soon as possible.
