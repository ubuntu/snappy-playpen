# Cloud Foundry CLI snap

This is a CLI go project for managing Cloud Foundry applications.
There is a deb package, but it is not in the Ubuntu archive nor in a PPA.

## Current state

Working features:
 - The snap builds and executes. More testing is required to verify the functions don't
   require extra interfaces.

Known issues:
 - It required to hack the go plugin in order to install only the main package.
 - The project has a script to generate localization messages. That is not being run in this package.
