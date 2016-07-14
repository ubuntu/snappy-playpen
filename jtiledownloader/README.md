# jTileDownloader snap

This project creates a working snap of
[jTileDownloader](http://wiki.openstreetmap.org/wiki/JTileDownloader), a Java
app to download OpenStreetMap tiles for offline map caching.

Snapping inspired by [uNav's instructions for offline
caching](https://unav-go.github.io/offline/).

There is an [alternative approach to creating the snap](https://github.com/ogra1/jtiledownloader), by Oliver Grawert.

To get this done, we need to do the following:
 - use the copy plugin to download and unpack a .zip file into a .jar file
 - use a custom launcher to set up the environment variables required for
   Java and use `java -jar` to execute the .jar file

## Current state

Working features:
 - Tested in confined mode
 - App GUI starts and downloads tiles as expected

Known issues:
 - The app tries to create an appConfig.xml file upon each start. It would be
   nice to instruct it to create it in a writable location.
 - Tiles download requests are blocked if you use the Mapnik server, but this seems to be an issue
   with the external server. Same issue happens if you run the app manually outside the snap.

TODO:
 - Theming support needs improvement, perhaps we need a
   desktop launcher for Java apps
 
