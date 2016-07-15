# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
import os
from subprocess import Popen, PIPE

import snapcraft
from snapcraft.plugins import copy

class TexLivePlugin(snapcraft.plugins.copy.CopyPlugin):

    def build(self):
        super(copy.CopyPlugin, self).build()

        # Install TexLive with the standard installer
        env = self._build_environment()
        #self.run(['{}/install-tl'.format(self.builddir), '-scheme', 'basic'], env=env)
        p1 = Popen(['echo', '-n', 'I'], env=env, stdout=PIPE)
        p2 = Popen(['{}/install-tl'.format(self.builddir), '-portable', '-scheme', 'basic'], env=env, stdin=p1.stdout, stdout=PIPE)
        output = p2.communicate()[0]


    def _build_environment(self):
        env = os.environ.copy()
        env['TEXLIVE_INSTALL_PREFIX'] = os.path.join(self.installdir, 'usr', 'local')
        return env
