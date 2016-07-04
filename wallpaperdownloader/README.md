# WallpaperDownloader snap

This project creates a working snap of the WallpaperDownloader application.
WallpaperDownloader is a simple GUI Java-based application to download wallpapers from the Internet and manage them. 
For more information, please visit the official [Wiki](https://bitbucket.org/eloy_garcia_pca/wallpaperdownloader/wiki/Home) of the project.

## Current state

Working features:
 - The application is working fine. You can even change the downloads folder (by default inside snap directory) to a directory within the user's home folder.
 - Now, the application is integrated with the Desktop. A Desktop Launcher has been created and a menu entry too under `Utility` category.

Known issues:
  - Open `downloads folder` button is not working. An exception is thrown: 

      Error trying to open the Downloads directory. Error: Failed to show URI:file:/home/egarcia/snap/wallpaperdownloader/1/.wallpaperdownloader/downloads/)
