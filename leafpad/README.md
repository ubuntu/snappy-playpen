# leafpad snap

This project creates a working snap of `leafpad`.

To get this done, we need to do the following:
 - add custom launcher (stolen from
   http://bazaar.launchpad.net/~didrocks/+junk/galculator-snap/view/head:/galculator.wrapper)
 - use the `leafpad` git tree (https://github.com/oluc/leafpad)

## Current state

Working features:
 - it generally works

Known issues:
  - needs to be connected to the `home` slot to access your files, ie:
    ```
    sudo snap connect leafpad:home ubuntu-core:home
    ```
