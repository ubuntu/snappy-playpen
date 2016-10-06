# consul snap

This project creates a working snap of hashicorp's consul.
This is a go project for discovering and configuring services.
It is used a lot in docker deployments. It is in the yakkety archive, but not in
xenial.

## Current state

Working features:
 - The steps mentioned in https://www.consul.io/intro/getting-started/*

## Notes:

You can use healthcheck-toolbox-example snap for adding some checkers utility
like curl enablement. This one will be downloaded from the store, installed and
connected automatically if no other snap on your system provides
healthcheck-toolbox content interface on your system.

If you want to add a ping health check, you need to connect to network-observe
slot from the core snap.

A vagrant file is always provided to follow the getting-started intro on
a snap system, based on ubuntu:
https://www.consul.io/intro/getting-started/join.html.
