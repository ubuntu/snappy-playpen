# Mesa-demos snap

This project creates a working snap of the [mesa/demos](https://cgit.freedesktop.org/mesa/demos) repository. It includes many applications using the OpenGL, OpenGL|ES 1.1, OpenGL|ES 2.0, EGL APIs.

The main aim is to use these demos as a tool to develop opengl, opengles and related interfaces in snapd.

## Current state

Working features:
  - Currently the following applications have been enabled in the snap :
      teapot
      gears
      tunnel2
      es2info
      es2tri
      es2gears
  
Known issues:
  - Only validated with Intel (i965, i915) GPU drivers, so far.
  - Only a few of the demos are included in the snap. Currently, each demo requires an env var to be set which is achieved through a wrapper. Having [lp:1583259](https://bugs.launchpad.net/snappy/+bug/1583259) would help when adding the others wholesale.
  - 'strict' mode is not yet supported as there are some seccomp denials due to 'sendmsg'. Needs more investigation as to whether a rule addressing that needs to be added to the 'opengl' interface or another interface needs to be created for glut, glx, etc that opengl apps typically use.

TODO:
 - Validate on post-Xenial
 - Validate on non-Intel GPUs
 - Add other demos once [lp:1583259](https://bugs.launchpad.net/snappy/+bug/1583259) is available
