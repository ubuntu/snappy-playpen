# -*- coding: utf-8 -*-

from snapcraft.plugins import nodejs


class WechatPlugin(nodejs.NodePlugin):
    """A plugin for build Electronic WeChat."""

    def build(self):
        super().build()
        self._build_wechat_linux()

    def _build_wechat_linux(self):
        # build linux version in dist folder
        self.run(['npm', 'run', 'build:linux'])
        # copy the dist folder into install folder
        self.run(['cp', '-r', '{}/dist'.format(self.builddir), self.installdir])
