---
file: etherpad-lite/README.md
title: Etherpad-lite
author: Winael
status: WIP. Not working
---

Etherpad-lite
=============

This project is about creating a snap of etherpad-lite, a coillaborative text-editor.

To talk and collaborate, you can join the Telegram group [Etherpad-lite-Playpen-Snappy][1]

Status
------

- Builds and installs fine
- Needs to be installed with --devmode
- Throws a RangeError: Maximum call stack size exceeded when launched. Any help from nodejs experts or tips on how to debug node apps welcome!

````bash
$ sudo /snap/bin/etherpad-lite
[2016-06-21 13:24:32.693] [WARN] console - DirtyDB is used. This is fine for testing but not recommended for production.
/snap/etherpad-lite/x1/lib/node_modules/ep_etherpad-lite/static/js/pluginfw/plugins.js:112
        if (name.indexOf(exports.prefix) === 0) {
                 ^

RangeError: Maximum call stack size exceeded
    at String.indexOf (native)
    at /snap/etherpad-lite/x1/lib/node_modules/ep_etherpad-lite/static/js/pluginfw/plugins.js:112:18
    at Function._.each._.forEach (/snap/etherpad-lite/x1/lib/node_modules/ep_etherpad-lite/node_modules/underscore/underscore.js:153:9)
    at _.(anonymous function) [as each] (/snap/etherpad-lite/x1/lib/node_modules/ep_etherpad-lite/node_modules/underscore/underscore.js:1496:34)
    at flatten (/snap/etherpad-lite/x1/lib/node_modules/ep_etherpad-lite/static/js/pluginfw/plugins.js:111:28)
    at /snap/etherpad-lite/x1/lib/node_modules/ep_etherpad-lite/static/js/pluginfw/plugins.js:120:52
    at Function._.each._.forEach (/snap/etherpad-lite/x1/lib/node_modules/ep_etherpad-lite/node_modules/underscore/underscore.js:153:9)
    at _.(anonymous function) [as each] (/snap/etherpad-lite/x1/lib/node_modules/ep_etherpad-lite/node_modules/underscore/underscore.js:1496:34)
    at flatten (/snap/etherpad-lite/x1/lib/node_modules/ep_etherpad-lite/static/js/pluginfw/plugins.js:111:28)
    at /snap/etherpad-lite/x1/lib/node_modules/ep_etherpad-lite/static/js/pluginfw/plugins.js:120:52
````

Roadmap
-------

### 1.0:

- Made Etherpad-lite working by himself (find how to copy entire folders)

### 2.0:

- Integrate MariaDB database instead of dirtydb

### 3.0:

- Add a web-interface to configure/administrate etherpad-lite

Original documentation
----------------------

The original documentation about how to install Etherpad could be find [here][2]

Architecture
------------

### Components

To build etherpad-lite we need :

  - A webserver
  - Etherpad-lite itself
  - A better database than dirty-db like MariaDB 
  - A config forms for Webdm [Optional]

### Interfaces

This snap needs to connect to internet, as a client and server, and export documents to the user home folder. 

So basically, the interfaces needed are :

  - network
  - network-bind
  - home

````yaml
  interfaces:
    - network
    - network-bind
    - home
````

### Parts

#### etherpad-lite

- `plugin`: Etherpad-lite is a node.js app. So we need to use the `nodejs` plugin.
- `source`: According to the official documentation, Etherpad-lite is host on GitHub. The source is git://github.com/ether/etherpad-lite
- `source-subdir`: `nodejs` plugin need that source subdirectory has been specified to be able to build the part. the source of etherpad-lite will be pulled in the `src` subdirectory
- `stage-packages`: According to the official documentation `gzip`, `git`, `curl`, `python`, `libssl-dev`, `pkg-config` and `build-essential`packages are needed to build etherpad-lite and are required by a script. 

````yaml
  etherpad-lite:
    plugin: nodejs
    source: git://github.com/ether/etherpad-lite
    source-subdir: src
    stage-packages: 
      - gzip 
      - git 
      - curl 
      - python 
      - libssl-dev 
      - pkg-config 
      - build-essential
````

[1]: https://telegram.me/EtherpadLitePlaypenSnappy
[2]: https://github.com/ether/etherpad-lite#installation
