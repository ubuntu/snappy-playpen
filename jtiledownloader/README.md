# jTileDownloader snap

This project creates a working snap of
[jTileDownloader](http://wiki.openstreetmap.org/wiki/JTileDownloader), a Java
app to download OpenStreetMap tiles for offline map caching.

Snapping inspired by [uNav's instructions for offline
caching](https://unav-go.github.io/offline/).

To get this done, we need to do the following:
 - use the copy plugin to download and unpack a .zip file into a .jar file
 - use a custom launcher to set up the environment variables required for
   Java and use `java -jar` to execute the .jar file

## Current state

Working features:
 - Tested in devmode only
 - App GUI starts
 - Tiles download requests seem to be blocked, but this seems to be an issue
   with the app running outside the snap too

Known issues:
 - Theming does not work.
 - The app tries to create an appConfig.xml file upon each start. It would be
   nice to instruct it to create it in a writable location.

TODO:
 - Add a desktop file and icon to launch it from the dash
 - Theming support needs improvement, perhaps we need a
   desktop launcher for Java apps
 
