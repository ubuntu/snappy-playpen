# nginx snap

This is work in progress to create the nginx snap.
nginx is an HTTP and reverse proxy server, a mail proxy server, and a generic
TCP/UDP proxy serve.

## Current state

Working features:
 - The server starts in devmode.

Known issues:
 - The default configuration and log paths are defined at build time. We can't
   pass $SNAP and $SNAP_DATA to form those paths during the build, so currently,
   in order to run it we need to pass -c and create the log directories in the
   current directory.
 - The binary has to be run as root.
