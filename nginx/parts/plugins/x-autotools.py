"""This is a modified version of snapcraft's autotools plugin.

It calls the ./auto/configure of nginx.

    - configflags:
      (list of strings)
      configure flags to pass to the build such as those shown by running
      './auto/configure --help'
"""

import snapcraft


class AutotoolsPlugin(snapcraft.BasePlugin):

    @classmethod
    def schema(cls):
        schema = super().schema()
        schema['properties']['configflags'] = {
            'type': 'array',
            'minitems': 1,
            'uniqueItems': True,
            'items': {
                'type': 'string',
            },
            'default': [],
        }

        # Inform Snapcraft of the properties associated with building. If these
        # change in the YAML, Snapcraft will consider the build step dirty.
        schema['build-properties'].extend(['configflags'])

        return schema

    def __init__(self, name, options, project):
        super().__init__(name, options, project)
        self.build_packages.extend([
            'autoconf',
            'automake',
            'autopoint',
            'libtool',
            'make',
        ])

    def build(self):
        super().build()
        configure_command = ['./auto/configure']
        make_install_command = ['make', 'install']

        # Use an empty prefix since we'll install via DESTDIR
        configure_command.append('--prefix=')
        make_install_command.append('DESTDIR=' + self.installdir)

        self.run(configure_command + self.options.configflags)
        self.run(['make', '-j{}'.format(self.parallel_build_count)])
        self.run(make_install_command)

    def snap_fileset(self):
        fileset = super().snap_fileset()
        # Remove .la files which don't work when they are moved around
        fileset.append('-**/*.la')
        return fileset
