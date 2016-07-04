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
