# healthcheck-toolbox-example snap

This project creates a healthcheck-toolbox-example collection to be used
as a slot via content interfaces for providing health check tools.
This one can be consumed by hashicorp's consul for instance.

## Current state

Working features:
 - curl is working from this snap. It only makes sense in a connected context
   to another snap.
