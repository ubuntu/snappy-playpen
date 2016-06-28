# ImageMagick7-edge snap

This project creates a mostly-working snap of kitchen-sink (all options)
ImageMagick 7.

To get this done, we need to do the following:
 - Find out what doesn't work yet; I am not a server admin and have no
   real workloads to test with. Having run `imagemagick-edge.mogrify` on
   a directory of images, I can confirm basic functionality, however
   `imagemagick-edge.magick / magick-script` don't work. I don't know how
   they are usually used, and what I might be doing wrong, or if there are
   serious errors to be addressed.
  
 - Give feedback about missing options, and if you know how to enable
   them, let me know
 - Develop a solid, working security profile, and determine the `snap`
   interfaces required

## Current state

Working features:
 - Builds the `snap` of IM7 and provides access to all tools through
   `imagemagick-edge.<tool>`

Known issues:
 - The main CLI tools (`convert`, `conjure`, `mogrify`, `identify`, etc)
   work, but default unconfigured security permissions just block any
   reading of files. This is current normal behaviour for any `snap`
   installed application. Installation instructions below.

TODO:
 - Security profile
 - Upload to store on correct `edge` channel - would prefer more
   auditing before making this more widely available, or having project
   maintainers take the initiative from the start.
 
#### Installation Instructions

Like any program in the `snappy-playpen` which isn't in the `snappy
store`, clone the `ubuntu/snappy-playpen` repository, and run `$ snapcraft
cleanbuild` in the project's directory. After waiting a while and building
the `.snap` for yourself. Complete command walkthrough, requires Ubuntu
16.04, `git`,`lxd`, `snapcraft', and an UbuntuOne account for zero-hassle
installation and removal of snaps (no need for `sudo`)

```

    $ git clone git://github.com/ubuntu/snappy-playpen
    $ cd snappy-playpen/imagemagick-edge/
    $ snap login <your@ubuntu.one.email>
        <authenticate>
    $ snapcraft cleanbuild
        <lots of compiling>
    $ snap install imagemagick-edge.snap
    $ snap connect imagemagick-edge:home ubuntu-core:home

```
