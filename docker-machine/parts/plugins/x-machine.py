# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright (C) 2015 Canonical Ltd
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

"""This plugin extends the go plugin to add a bulid path

This plugin uses the common plugin keywords, for more information check the
'plugins' topic.

This plugin uses the common plugin keywords as well as those for "sources".
For more information check the 'plugins' topic for the former and the
'sources' topic for the latter.

Additionally, this plugin uses the following plugin-specific keywords:

    - go-packages:
      (list of strings)
      Go packages to fetch, these must be a "main" package. Dependencies
      are pulled in automatically by `go get`.
      Packages that are not "main" will not cause an error, but would
      not be useful either.

    - go-importpath:
      (string)
      This entry tells the checked out `source` to live within a certain path
      within `GOPATH`.
      This is not needed and does not affect `go-packages`.

    - go-buildpath:
      (string)
      This entry is the path of the file to be build and installed.
"""

import logging
import os

from snapcraft.plugins import go


logger = logging.getLogger(__name__)


class MachinePlugin(go.GoPlugin):

    @classmethod
    def schema(cls):
        schema = super().schema()
        schema['properties']['go-buildpath'] = {
            'type': 'string',
            'default': ''
        }
        # Inform Snapcraft of the properties associated with building. If these
        # change in the YAML Snapcraft will consider the build step dirty.
        schema['build-properties'].extend(['source', 'go-buildpath'])

        return schema

    def _local_build(self):
        if self.options.go_buildpath:
            return self._run(
                ['GOBIN={}'.format(os.path.join(self.installdir, 'bin')),
                 'go', 'install',
                 os.path.join(self.sourcedir, self.options.go_buildpath)])

        elif self.options.go_importpath:
            go_package = self.options.go_importpath
        else:
            go_package = os.path.basename(os.path.abspath(self.options.source))
        self._run(['go', 'install', './{}/...'.format(go_package)])
