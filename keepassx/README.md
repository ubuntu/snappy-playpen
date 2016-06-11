# keepassx snap

This project creates a working snap of keepassx.
This is a qt5 project to manage passwords.

## Current state

Working features:
 - everything in x86_64

Known issues:
 - the password database file is likely to be stored in the user's home, or a
   location that's synchronized between machines and to the cloud. People are
   not likely to store the file in the snap data directory.
 - the theming is not the same as the other system apps.
 - the giomodule and gschemas files were copied from an ubuntu classic system,
   because they are generated after the deb is installed.
 - I don't understand why it needs libqt4-dev to find qt5-core in cmake.
