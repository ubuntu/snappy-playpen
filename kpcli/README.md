# kpcli snap

This project creates a working snap of keepass cli.
This is a perl command line project, to manage passwords and secrets.

## Current state

Working features:
 - everything in x86_64

Known issues:
 - the `run.sh` script has some hardcoded perl paths, which makes this
   non-multiarchitecture, and won't nicely support other perl versions.
 - the password database file is likely to be stored in the user's home, or a
   location that's synchronized between machines and to the cloud. People are
   not likely to store the file in the snap data directory.
