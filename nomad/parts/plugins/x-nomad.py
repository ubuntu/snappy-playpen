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

"""This is a modifyied version of snapcraft's go and make plugins.

It uses code from  the go plugin to pull, and the make plugin to build and
install.

"""
import os
import shutil

from snapcraft import BasePlugin
from snapcraft.plugins import go


class NomadPlugin(go.GoPlugin):

    def build(self):
        BasePlugin.build(self)
        command = ['make']

        self._run_make(command + ['bootstrap'])
        self._run_make(command + [
            'dev', '-j{}'.format(self.project.parallel_build_count)])
        shutil.copy(
            os.path.join(self._gopath_bin, 'nomad'), self.installdir)

    def _run_make(self, cmd, **kwargs):
        env = [
            'env',
            'GOPATH={}'.format(self._gopath),
            'PATH={}:{}'.format(os.getenv('PATH'), self._gopath_bin),
        ]
        cwd = os.path.join(self._gopath_src, self.options.go_importpath)
        return self.run(env + cmd, cwd=cwd, **kwargs)
