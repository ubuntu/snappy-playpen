# ectd snap

This is a go project for distributed, consistent key-value store for shared configuration and service discovery.

etcd uses the Raft consensus algorithm to manage a highly-available replicated log.

## Current state

Working features:
 - etdctl builds and runs

To do:
 - Figure out the interfaces required to remove devmode.
 - More testing is required for etcdctl

Known issues:
 - etdctl is build from the package, not from the tag.
 - etcd daemon is not building
