# ristretto snap

This project creates a working snap of `ristretto`.

To get this done, we need to do the following:
 - use desktop launcher part
 - build from current git

## Current state

Working features:
 - viewing/editing pictures

Known issues:
  - no thumbnailer service, even though tumbler is included
** (ristretto:11165): WARNING **: DBUS-call failed:The name
    org.freedesktop.thumbnails.Thumbnailer1 was not provided by
    any .service files
-> no lookup for .service files.

TODO:
 - fix tumbler issue
 
