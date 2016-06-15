# MATE Desktop snap

This project attempts to create a working snap of the complete MATE Desktop 
environment. The initial objective is to get just the main applications 
running.

This is a multi-part snap because the MATE packages in the Xenial archive are 
built against GTK2 and I want to test MATE git master built against GTK3.

## Current state

The components are listed in build order.

  * mate-common                 [ BUILDS ]
  * mate-desktop                [ EXECUTES ]
  * mate-user-guide             [ BUILDS ]
  * libmatekbd                  [ FAILS ]
  * libmatemixer                [ BUILDS ]
  * libmateweather
  * mate-icon-theme             [ CONFLICTS ]
  * caja
  * mate-polkit
  * marco
  * mate-settings-daemon
  * mate-session-manager
  * mate-menus
  * mate-panel
  * mate-backgrounds
  * mate-themes
  * mate-notification-daemon
  * mate-control-center
  * mate-screensaver
  * mate-media
  * mate-power-manager
  * mate-system-monitor         [ BUILDS ]
  * atril
  * caja-dropbox
  * caja-extensions
  * engrampa
  * eom
  * mate-applets
  * mate-icon-theme-faenza
  * mate-indicator-applet
  * mate-netbook
  * mate-sensors-applet
  * mate-terminal
  * mate-user-share
  * mate-utils
  * mozo
  * pluma                       [ BUILDS ]
  * python-caja

## FTBFS

### libmatekbd

Can't find `libmatedesktop-2.0`, complete error message will be added here in 
due course.

## Conflicts

### mate-icon-theme

    Parts 'mate-user-guide' and 'mate-icon-theme' have the following file
    paths in common which have different contents: usr/sbin/update-icon-
    caches
