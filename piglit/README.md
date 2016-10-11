# piglit snap

This project answers the musical question
"How well does OpenGL work inside a snap?"

It also illustrates how to build up a snap from
three pieces: one for upstream python bits, one for
upstream C bits, and one for a wrapper.

It uses the log-observe plug so it can access dmesg
(so it can tell which test cases cause kernel error messages).

Finally, comments in snapcraft.yaml illustrate each kludge along
the way to the final gargantuan commandline (which probably
should be replaced with a small wrapper script specific to
this project).

Example usage:

First, do a very quick sanity check to make sure you can access the graphics card:

$ piglit run tests/sanity results/sanity
$ piglit summary console results/sanity

If that passes, try a ten-to-45-minute subset of the tests,
without parallelism, verbosely, and saving any dmesg errors:

$ piglit run -1 -v --dmesg --sync -t texture tests/quick results/quick
$ piglit summary console results/quick

That's enough to expose obviously bad graphics drivers,
and with some proprietary drivers, even lock up the system; see
https://devtalk.nvidia.com/default/topic/965768/piglit-opengl-conformance-test-seems-to-really-give-nvidia-drivers-grief-/

If you're serious about opengl testing, you'll want to run the rest of
the tests, but that's enough for starters.

See https://piglit.freedesktop.org/ for more about Piglit.
