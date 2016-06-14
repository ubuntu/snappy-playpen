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


import logging

import snapcraft

LOG = logging.getLogger(__name__)

class TUOMake(snapcraft.BasePlugin):
    """Fixup broken upstream build
    Add missing dir and fake missing install target
    """
    def __init__(self, name, options, project):
        super().__init__(name, options, project)

    def build(self):
        super().build()
        LOG.info("TUOMake: Fixup build environment")
        self.run(['mkdir', '-p', 'obj'])
        LOG.info("TUOMake: Build")
        self.run(['make'] + ['-j{}'.format(self.project.parallel_build_count)])
        targetdir = self.installdir+'/usr/bin'
        LOG.info("TUOMake: Fake install")
        self.run(['cp', 'tuo.exe', targetdir])
        self.run(['cp', 'update_xml.sh', targetdir])
        LOG.info("TUOMake: Finished")
