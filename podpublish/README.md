# podpublish

A tool for encoding and publishing podcast content and assets. Inspired
by [bv-publish](https://github.com/stuartlangridge/bv-publish) and the
talk [Stuart Langridge gave at Oggcamp 2015](https://www.youtube.com/watch?v=IG6-YdBbwE8).

Project created by [Ubuntu Podcast](http://www.ubuntupodcast.org) and
released under the [GPLv2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
license.

  * https://bitbucket.org/flexiondotorg/podpublish

## Ubuntu Podcast Setup

The Snap `home` interface munges `${HOME}` and my use cae for podpublish is to 
use configuration files that contain relative paths to podcast assets, such as 
audio files and artwork.

The Ubuntu Podcast team use Dropbox to sync all the show assets, therefore the 
Dropbox directory needs to be symlinked into the podpublish snap data 
directory.

Run the following, which will create the data directory.

    /snap/bin/podpublish.encode-podcast --version

Now symlink Dropbox.

    ln -s ~/Dropbox ~/snap/podpublish/x{*}/

## Use

To encode a podcast.

    /snap/bin/podpublish.encode_podcast ~/Dropbox/UbuntuPodcast/Configs/S09/s09exx.ini

To upload a podcast.
 
    /snap/bin/podpublish.publish_podcast ~/Dropbox/UbuntuPodcast/Configs/S09/s09exx.ini
