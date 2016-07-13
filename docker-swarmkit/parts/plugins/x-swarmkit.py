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

"""This plugin extends the go plugin to workaround an issue with a
windows dependency."""

import logging
import os

from snapcraft.plugins import go


logger = logging.getLogger(__name__)


class SwarmkitPlugin(go.GoPlugin):

    def _local_build(self):
        if self.options.go_importpath:
            go_package = self.options.go_importpath
        else:
            go_package = os.path.basename(os.path.abspath(self.options.source))
        cmd_dir = os.path.join(self._gopath_src, go_package, 'cmd')
        for cmd in os.listdir(cmd_dir):
            self._run(['go', 'install', './{}'.format(
                os.path.join(go_package, 'cmd', cmd))])
