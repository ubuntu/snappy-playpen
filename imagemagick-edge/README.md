# ImageMagick7-edge snap

This project creates a mostly-working snap of kitchen-sink (all options)
ImageMagick 7.

To get this done, we need to do the following:
 - Find out what doesn't work yet; I am not a server admin and have no
   workloads to test with. Also, this is the next-gen ImageMagick and 
   I'm not really sure what changes in workflow will be there or not.
 - Give feedback about missing options, and if you know how to enable
   them, let me know
 - Develop a solid, working security profile, and determine the `snap`
   interfaces required

## Current state

Working features:
 - Builds the `snap` of IM6 and provides access to all tools through
   `imagemagick-edge.<tool>`

Known issues:
 - The main CLI tools (`convert`, `conjure`, `mogrify`, `identify`, etc)
   can't access any files at all, the unconfigured security profile blocks
   the process reading any files at all

TODO:
 - Security profile
 - Upload to store on correct `edge` channel
