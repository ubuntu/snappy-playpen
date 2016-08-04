# vault snap

This project creates a working snap of hashicorp's vault.
This is a CLI go project for handling secrets. So the way go handles
dependencies and the fact that it's a security tool that needs to be always
up-to-date make it a nice use case for snappy.

## Current state

Working features:
 - Testing in progress: https://gist.github.com/elopio/e8481471a9b3964ccf5bf9f0c09605a9

Known issues:
 - only uploaded to the store for amd64.
