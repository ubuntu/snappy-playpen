# Nomad snap

This is a complex project written in go project, for managing clusters.
Version 0.4.0 has just been released with binaries to execute in linux, but no
packages for any distribution so no way to get updates easily. Also, it required
a custom plugin that's a mix of go and make.

## Current state

Working features:
 - The agent starts in devmode. More testing is needed to test all the features.

Known issues:
 - In strict mode, it fails with:
   Error starting agent: client setup failed: fingerprinting failed: Failed to
   discover cgroup mount point: open /proc/self/mountinfo: permission denied
 - The project uses gox to generate binaries for multiple architectures, maybe
   we could use that too for cross-compiling.
