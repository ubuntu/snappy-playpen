# podpublish

A tool for encoding and publishing podcast content and assets. Inspired
by [bv-publish](https://github.com/stuartlangridge/bv-publish) and the
talk [Stuart Langridge gave at Oggcamp 2015](https://www.youtube.com/watch?v=IG6-YdBbwE8).

Project created by [Ubuntu Podcast](http://www.ubuntupodcast.org) and
released under the [GPLv2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
license.

  * https://bitbucket.org/flexiondotorg/podpublish

## Current state

`podpublish` builds and nearly works. When trying to encode a podcast `ffmpeg` 
throws the error below, but `libpulsecommon-8.0.so` is in the snap.

    Traceback (most recent call last):
      File "/snap/podpublish/x1/usr/bin/encode-podcast", line 9, in <module>
        load_entry_point('PodPublish==0.0.0', 'console_scripts', 'encode-podcast')()
      File "/snap/podpublish/x1/usr/lib/python3/dist-packages/PodPublish-0.0.0-py3.5.egg/podpublish/encode_podcast.py", line 20, in main
        encoder.audio_encode(config, 'mp3')
      File "/snap/podpublish/x1/usr/lib/python3/dist-packages/PodPublish-0.0.0-py3.5.egg/podpublish/encoder.py", line 36, in audio_encode
        AudioSegment.from_file(config.audio_in).export(audio_file,
      File "/snap/podpublish/x1/usr/lib/python3/dist-packages/pydub/audio_segment.py", line 446, in from_file
        raise CouldntDecodeError("Decoding failed. ffmpeg returned error code: {0}\n\nOutput from ffmpeg/avlib:\n\n{1}".format(p.returncode, p_err))
    pydub.exceptions.CouldntDecodeError: Decoding failed. ffmpeg returned error code: 127
    
    Output from ffmpeg/avlib:
    
    b'ffmpeg: error while loading shared libraries: libpulsecommon-8.0.so: cannot open shared object file: No such file or directory\n'

Also, depending on where the show assets are located, some symlinking maybe 
required.

## Install

The Snap `home` plug doesn't expose the user home directory, just an isolsated 
data directory. The Ubuntu Podcast team use Dropbox to sync all the show 
assets, therefore the Dropbox directory needs to be symlinked into the `podpublish`
snap data directory.

Run the following, which will create the data directory.

    /snap/bin/podpublish.encode-podcast --version

Now symlink Dropbox.

    ln -s ~/Dropbox ~/snap/podpublish/x{*}/

## Use

To encode a podcast.

    /snap/bin/podpublish.encode_podcast ~/Dropbox/UbuntuPodcast/Configs/S09/s09exx.ini

To upload a podcast.
 
    /snap/bin/podpublish.publish_podcast ~/Dropbox/UbuntuPodcast/Configs/S09/s09exx.ini
