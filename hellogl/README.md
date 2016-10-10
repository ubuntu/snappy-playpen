# hellogl snap

This project creates a very small snap that demonstrates using OpenGL.
It bundles a small wrapper called opengl-launcher which sets
LIBGL_DRIVERS_PATH to avoid the runtime error
libGL error: unable to load driver: i965_dri.so
(see https://bugs.launchpad.net/snappy/+bug/1584178 )
Hopefully the default snap wrapper will do that someday,
but until then, this demo is a tiny example of how
to work around that problem.

If you're already bundling gtk or Qt, you don't need the workaround,
as desktop-launch already sets LIBGL_DRIVERS_PATH.
But bundling gtk or Qt greatly increases snap size,
and seems to cause a minute-long startup delay on
first run (it runs update-mime-database?).
So avoiding it is nice for simple apps that don't need it.
