# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-

from contextlib import suppress
import glob
import os
import re
import fileinput

import snapcraft
from snapcraft.plugins import copy
from snapcraft.plugins.copy import _recursively_link


class CopyAndEditPlugin(copy.CopyPlugin):

    @classmethod
    def schema(cls):
        schema = super().schema()

        schema['properties']['edit'] = {
            'type': 'object',
        }

        # Inform Snapcraft of the properties associated with building. If these
        # change in the YAML Snapcraft will consider the build step dirty.
        schema['build-properties'].append('edit')

        return schema

    def build(self):
        # setup build directory
        super(copy.CopyPlugin, self).build()

        files = self.options.files
        editables = self.options.edit
        globs = {f: files[f] for f in files if glob.has_magic(f)}
        filepaths = {os.path.join(self.builddir, f): files[f] for f in files
                     if not glob.has_magic(f)}

        for edit in editables:
            fpath = os.path.join(self.builddir, edit)
            if os.path.exists(fpath):
                for regex in editables[edit]:
                    for line in fileinput.input([fpath], inplace=True):
                        r = re.compile(regex)
                        print (r.sub(editables[edit][regex], line.rstrip()))

        for src in globs:
            paths = glob.glob(os.path.join(self.builddir, src))
            if not paths:
                raise EnvironmentError('no matches for {!r}'.format(src))
            for path in paths:
                filepaths.update(
                    {os.path.join(self.builddir, path): globs[src]})

        for src in sorted(filepaths):
            dst = os.path.join(self.installdir, filepaths[src].lstrip('/'))
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            _recursively_link(src, dst, self.installdir)


# patch _link_or_copy as some symlinks could be written by edit or replace
_original_link_or_copy = copy._link_or_copy
def new_link_or_copy(*args, **kwargs):
    with suppress(FileExistsError):
        _original_link_or_copy(*args, **kwargs)
copy._link_or_copy = new_link_or_copy
