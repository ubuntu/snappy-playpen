from snapcraft.plugins import go


class CFPlugin(go.GoPlugin):

    def _local_build(self):
        self._run(['go', 'install', './{}/...'.format(
            'github.com/cloudfoundry/cli/main')])
