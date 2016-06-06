Etherpad-lite
=============

This project is about creating a snap of etherpad-lite, a coillaborative text-editor.

To talk and collaborate, you can join the Telegram group [Etherpad-lite-Playpen-Snappy][1]
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

### Parts

#### etherpad-lite

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

- `plugin`: Etherpad-lite is a node.js app. So we need to use the `nodejs` plugin.
- `source`: According to the official documentation, Etherpad-lite is host on GitHub. The source is git://github.com/ether/etherpad-lite
- `source-subdir`: `nodejs` plugin need that source subdirectory has been specified to be able to build the part. the source of etherpad-lite will be pulled in the `src` subdirectory
- `state-packages`: According to the official documentation `gzip`, `git`, `curl`, `python`, `libssl-dev`, `pkg-config`and `build-essential`packages are needed to build etherpad-lite. 

##### Source



Snapcraft.yaml
---------------



[1]: https://telegram.me/EtherpadLitePlaypenSnappy
[2]: https://github.com/ether/etherpad-lite#installation
