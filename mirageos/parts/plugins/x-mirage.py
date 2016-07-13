# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright (C) 2015, 2016 Canonical Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""This plugin extends the make plugin to install opam depencencies.

This plugin uses the common plugin keywords as well as those for "sources".
For more information check the 'plugins' topic for the former and the
'sources' topic for the latter.

Additionally, this plugin uses the following plugin-specific keyword:

    - makefile:
      (string)
      Use the given file as the makefile.

    - make-parameters:
      (list of strings)
      Pass the given parameters to the make command.

    - opam-packages:
      (list of strings)
      A list of dependencies to get from OPAM.
"""

import os
import shutil

from snapcraft import BasePlugin
from snapcraft.plugins import make


class MiragePlugin(make.MakePlugin):

    @classmethod
    def schema(cls):
        schema = super().schema()
        schema['properties']['opam-packages'] = {
            'type': 'array',
            'minitems': 1,
            'uniqueItems': True,
            'items': {
                'type': 'string'
            },
            'default': [],
        }

        # Inform Snapcraft of the properties associated with building. If these
        # change in the YAML Snapcraft will consider the build step dirty.
        schema['build-properties'].extend(['opam-packages'])

        return schema

    def __init__(self, name, options, project):
        super().__init__(name, options, project)
        self._opam_dir = os.path.join(self.partdir, 'opam')

    def pull(self):
        super().pull()
        os.makedirs(self._opam_dir, exist_ok=True)

    def clean_pull(self):
        super().clean_pull()

        # Remove the opam directory (if any)
        if os.path.exists(self._opam_dir):
            shutil.rmtree(self._opam_dir)

    def build(self):
        BasePlugin.build(self)

        root = '--root={}'.format(self._opam_dir)
        self.run(['opam', 'init', '--auto-setup', root])

        # XXX we could install the dependencies from the .opam file, but I
        # didn't find how to pass a file to opam install.
        # --elopio - 2016-07-08
        for pkg in self.options.opam_packages:
            self.run(['opam', 'install', '-y', root, pkg])

        command = ['opam', 'config', root, 'exec', '--', 'make']

        if self.options.makefile:
            command.extend(['-f', self.options.makefile])

        if self.options.make_parameters:
            command.extend(self.options.make_parameters)

        self.run(command +
                 ['OPAMROOT={}'.format(self._opam_dir),
                  'PREFIX={}'.format(self.installdir),
                  '-j{}'.format(self.project.parallel_build_count)])
        self.run(command + ['install'])
