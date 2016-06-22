# ImageMagick6-stable snap

This project creates a mostly-working snap of kitchen-sink (all options)
ImageMagick 6.

To get this done, we need to do the following:
 - Find out what doesn't work yet; I am not a server admin and have no
   real workloads to test with. Having run `imagemagick-stable.mogrify` on
   a directory of images, I can confirm basic functionality, so everything
   _should_ work.
 - Give feedback about missing options, and if you know how to enable
   them, let me know (ie, OpenCL... no idea if that is relevant in
   a server context)
 - Develop a solid, working security profile, and determine the `snap`
   interfaces required

## Current state

Working features:
 - Builds the `snap` of IM6 and provides access to all tools through
   `imagemagick-stable.<tool>`

Known issues:
 - The main CLI tools (`convert`, `conjure`, `mogrify`, `identify`, etc)
   work, but default unconfigured security permissions just block any
   reading of files. This is current normal behaviour for any `snap`
   installed application. Installation instructions below.

TODO:
 - Security profile: using `snappy-debug.security scanlog` to monitor
   read/write activity of `imagemagick-stable.<operation>` it seems that
   IM6 wants to write to `/etc/ImageMagick-stable/log.xml`, which is
   denied. Operations still work correctly, but this is
   a misconfiguration, and logging should be somewhere within the image's
   `$SNAP` prefix.
 - Upload to store on correct `stable` channel - would prefer more
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
    $ cd snappy-playpen/imagemagick-stable/
    $ snap login <your@ubuntu.one.email>
        <authenticate>
    $ snapcraft cleanbuild
        <lots of compiling>
    $ snap install imagemagick-stable.snap
    $ snap connect imagemagick-stable:home ubuntu-core:home

```
