# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
import os

import snapcraft
from snapcraft.plugins import copy

class TexLivePlugin(snapcraft.plugins.copy.CopyPlugin):

    def build(self):
        super(copy.CopyPlugin, self).build()

        # Install TexLive with the standard installer
        env = self._build_environment()
        self.run(['{}/install-tl'.format(self.builddir), '-scheme', 'basic'], env=env)


    def _build_environment(self):
        env = os.environ.copy()
        env['TEXLIVE_INSTALL_PREFIX'] = os.path.join(self.installdir, 'usr', 'local')
        return env
