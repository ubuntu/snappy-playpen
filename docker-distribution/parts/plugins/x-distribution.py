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

"""This plugin combines parts of the go and the make plugins.
The first for the pull, the second for the build.
"""

import logging
import os
import shutil

import snapcraft


logger = logging.getLogger(__name__)


class DistributionPlugin(snapcraft.BasePlugin):

    @classmethod
    def schema(cls):
        schema = super().schema()
        schema['properties']['go-importpath'] = {
            'type': 'string',
            'default': ''
        }
        return schema

    def __init__(self, name, options, project):
        super().__init__(name, options, project)
        self.build_packages.append('golang-go')
        self.build_packages.append('make')
        self._gopath = os.path.join(self.partdir, 'go')
        self._gopath_src = os.path.join(self._gopath, 'src')
        self._gopath_bin = os.path.join(self._gopath, 'bin')
        self._gopath_pkg = os.path.join(self._gopath, 'pkg')
        self.sourcedir = os.path.join(self._gopath_src,
                                      self.options.go_importpath)

    def env(self, root):
        # usr/lib/go/bin on newer Ubuntus, usr/bin on trusty
        env = [
            'GOPATH={}/go'.format(root),
            'CGO_LDFLAGS="$CGO_LDFLAGS ' + ' '.join([
                '-L{0}/lib',
                '-L{0}/usr/lib',
                '-L{0}/lib/{1}',
                '-L{0}/usr/lib/{1}',
                '$LDFLAGS']).format(root, self.project.arch_triplet) + '"',
        ]
        return env

    def pull(self):
        # use -d to only download (build will happen later)
        # use -t to also get the test-deps
        super().pull()
        os.makedirs(self._gopath_src, exist_ok=True)
        self._run(['go', 'get', '-t', '-d', './{}/...'.format(
            self.options.go_importpath)])

    def clean_pull(self):
        super().clean_pull()

        # Remove the gopath (if present)
        if os.path.exists(self._gopath):
            shutil.rmtree(self._gopath)

    def build(self):
        super().build()
        command = ['env', 'GOPATH={}'.format(self._gopath),
                   'make', 'PREFIX={}'.format(self.installdir), 'binaries']
        cwd = os.path.join(self._gopath_src, self.options.go_importpath)
        self.run(command + ['-j{}'.format(self.project.parallel_build_count)],
                 cwd=cwd)

    def clean_build(self):
        super().clean_build()

        if os.path.isdir(self._gopath_bin):
            shutil.rmtree(self._gopath_bin)

        if os.path.isdir(self._gopath_pkg):
            shutil.rmtree(self._gopath_pkg)

    def _run(self, cmd, **kwargs):
        cmd = ['env', 'GOPATH={}'.format(self._gopath)] + cmd
        return self.run(cmd, cwd=self._gopath_src, **kwargs)
