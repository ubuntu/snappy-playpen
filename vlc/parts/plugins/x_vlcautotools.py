# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-

import snapcraft
from snapcraft.plugins import autotools


class VLCAutotoolsPlugin(autotools.AutotoolsPlugin):

    def build(self):
        # setup build directory
        super(autotools.AutotoolsPlugin, self).build()

        # run boostrap before autotools build
        self.run(['./bootstrap'])

        # the plugins hooks are not idemnpotent, where they should be.
        # so we need to answer that calling the autotools plugins won't
        # retrigger BasePlugin build() which erase the directory.
        # However the issue with this hack is that other parts from this
        # project will be impacted if they are instantiated after this
        # method is ran, which is unlikely, but still possible.
        # https://bugs.launchpad.net/snapcraft/+bug/1595964.
        snapcraft.BasePlugin.build = lambda self: None
        super().build()
