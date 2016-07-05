# Cloud Foundry CLI snap

This is a CLI go project for managing Cloud Foundry applications.
There is a deb package, but it is not in the Ubuntu archive nor in a PPA.

## Current state

Working features:
 - The snap builds and executes. More testing is required to verify the functions don't
   require extra interfaces.

Known issues:
 - The branch has many main packages, which makes snapcraft fail unless a workaround is implemented:
   https://bugs.launchpad.net/snapcraft/+bug/1599328
 - The project has a script to generate localization messages. That is not being run in this package.
