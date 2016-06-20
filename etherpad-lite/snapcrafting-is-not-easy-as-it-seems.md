---
file: snapcrafting-is-not-easy-as-it-seems.md
title: Snapcrafting is not easy as it seems
author: Winael
date: 2016-06-20
tags: snapcraft, ubuntu, snaps, etherpad-lite
---

Few month ago, I'd like to try to create my first snap package. On the paper it seemed so simple to do it. Virtually can can take any project on github and with the help of few tools like Snapcraft and its pugins, tadaaaaa, you're creating a snap.

So, I thank, _"OK, I'll try to build snaps package from Framacloud services"_, and begun by the most popular of them, Etherpad-lite

# Meta-informations

First of all, when you created a snaps, you'll need to create a `snapcraft.yaml` file. It's your recipe to create your snap from differents sources as git ou bazaar repository.

You can generated one with the `snapcraft init` command that will create the `snapcraft.yaml`file based on a basic template

So basically, this is what meta-infos look like for this snap :

````yaml
name: etherpad-lite-unofficial
version: 0.1
summary: Etherpad-lite, really-real time collaborative editor
description: |
  Etherpad allows you to edit documents collaboratively in real-time, much like
  a live multi-player editor that runs in your browser. Write articles, press
  releases, to-do lists, etc. together with your friends, fellow students or
  colleagues, all working on the same document at the same time.

````

I use _etherpad-lite_ as a **name**, this is the **version** _0.1_, the **sumary** is a little sentences for the store list, and the description is needed for the store. Note that you can use the pipe symbols to write very long description
Studiying Etherpad-lite 
