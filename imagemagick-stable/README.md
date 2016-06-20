# ImageMagick6-stable snap

This project creates a mostly-working snap of kitchen-sink (all options)
ImageMagick 6.

To get this done, we need to do the following:
 - Find out what doesn't work yet; I am not a server admin and have no
   workloads to test with
 - Give feedback about missing options, and if you know how to enable
   them, let me know
 - Develop a solid, working security profile, and determine the `snap`
   interfaces required

## Current state

Working features:
 - Builds the `snap` of IM6 and provides access to all tools through
   `imagemagick-stable.<tool>`

Known issues:
 - The main CLI tools (`convert`, `conjure`, `mogrify`, `identify`, etc)
   seem like they work in a no-op situation, but default unconfigured
   security permissions just block any reading of files

TODO:
 - Security profile
 - Upload to store on correct `stable` channel
