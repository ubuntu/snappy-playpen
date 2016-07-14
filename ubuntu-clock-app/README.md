# ubuntu-clock-app snap

This project creates a working snap of ubuntu-clock-app.

To get this done, we need to do the following:
 - build from current bzr
 - add our own custom launcher, as we have to set
   `export QML2_IMPORT_PATH=$SNAP/usr/lib/$ARCH/qt5/qml/ClockApp`
   and we are somewhat blocked on [1602728][1602728] and [1602728][1602728]

## Current state

Working features:
 - all

Known issues:

 - we can't use the desktop/qt5 launcher yet
 - we need to slim down the package size 
