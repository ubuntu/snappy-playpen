# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright (C) 2016 Canonical Ltd
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


import glob
import logging
import os
import subprocess

import snapcraft

logger = logging.getLogger(__name__)


class QmakePlugin(snapcraft.BasePlugin):
    def __init__(self, name, options, project):
        super().__init__(name, options, project)

    def build(self):
        super().build()
        pwd = os.getcwd()
        os.chdir(self.builddir)
        self.run(['qmake-qt4', 'PREFIX=usr'])
        self.run(['make', '-e', 'PREFIX=usr'])
        self.run(['fakeroot', 'make', 'install', '-e', 'PREFIX=usr'])
        installdir = os.path.join(self.builddir, '../install')
        for f in glob.glob(self.builddir+'/*'):
            subprocess.check_call([
                'cp', '-ra', f, installdir])
        os.chdir(pwd)
