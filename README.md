# The snappy playpen

A place to test snapcraft, learn creating snaps and share best practices.

[Get started >](http://developer.ubuntu.com/desktop)

[Basic snap and snapcraft notions >](http://snapcraft.io/create/)

## Current project status
[![Build Status](https://api.travis-ci.org/ubuntu/snappy-playpen.svg?branch=master)](https://travis-ci.org/ubuntu/snappy-playpen) - **passing** means all snaps are automatically built correctly

This project currently includes the following snaps:

| State               | App                | Snap name in the store    | Uses                      |
| ------------------- | ------------------ | ------------------------- | ------------------------- |
| :white_check_mark:  | `2048`             |                           | qt5, qml, copy            |
| :white_check_mark:  | `atom`             | [atom-cwayne][atom]       | electron, grunt, nodejs   |
| :white_check_mark:  | `cloudfoundry-cli` |                           | go                        |
| :white_check_mark:  | `consul`           |                           | go                        |
| :white_check_mark:  | `click-parser`     | [click-parser][click-parser] | nodejs                 |
| :white_check_mark:  | `dcos-cli`         |                           | python3                   |
| :red_circle:        | `deis-workflow-cli`|                           | go                        |
| :white_check_mark:  | `dosbox`           |                           | autotools                 |
| :white_check_mark:  | `docker-compose`   |                           | python3                   |
| :white_check_mark:  | `ffmpeg`           |                           | autotools                 |
| :white_check_mark:  | `galculator`       |                           | autotools, gtk3           |
| :white_check_mark:  | `gitter-im`        |                           | copy, gtk3, wget          |
| :red_circle:        | `heroku`           |                           | go                        |
| :white_check_mark:  | `idea`             |                           | ant, antIntellij, java, openjdk |
| :white_check_mark:  | `imagemagick6-stable`|                         | autotools                 |
| :red_circle:        | `imagemagick7-git` |                           | autotools                 |
| :white_check_mark:  | `jtiledownloader`  | [jtiledownloader][]       | copy, jar, java           |
| :white_check_mark:  | `keepassx`         | [keepassx-elopio][]       | cmake, qt5                |
| :white_check_mark:  | `kpcli`            | [kpcli-elopio][kpcli]     | copy, perl                |
| :white_check_mark:  | `leafpad`          |                           | autotools, gtk2, lubuntu, xubuntu |
| :white_check_mark:  | `minetest`         |                           | cmake, copy               |
| :white_check_mark:  | `mirageos`         |                           | caml, opam, make              |
| :white_check_mark:  | `moon-buggy`       | [moon-buggy][moon-buggy]  | curses, autotools         |
| :white_check_mark:  | `mpv`              |                           | autotools, waf            |
| :white_check_mark:  | `openjdk-demo`     |                           | java, openjdk             |
| :white_check_mark:  | `openttd`          |                           | copy, qt5                 |
| :red_circle:        | `plank`            |                           | autotools, vala           |
| :white_check_mark:  | `qcomicbook`       |                           | cmake, qt5                |
| :red_circle:        | `qdriverstation`   |                           | frc, qmake, qt5, robotics |
| :white_check_mark:  | `qownnotes`        | [qownnotes][qownnotes]    | qmake, qt5, tar           |
| :white_check_mark:  | `ristretto`        |                           | qmake, qt5, tar           |
| :white_check_mark:  | `scummvm`          |                           | autotools                 |
| :white_check_mark:  | `shotwell`         |                           | autotools, vala           |
| :white_check_mark:  | `smplayer`         |                           | qt5, stage-package        |
| :white_check_mark:  | `tinyproxy`        |                           | copy, daemon, stage-package |
| :white_check_mark:  | `tyrant-unleashed-optimizer` |                 | make                      |
| :white_check_mark:  | `ubuntu-clock-app` | [ubuntu-clock-app][clock] | qmake, qt5                |
| :white_check_mark:  | `ubuntukylin-icon-theme` |                     | copy_and_edit, theme      |
| :white_check_mark:  | `vault`            | [vault-elopio][vault]     | go                        |
| :white_check_mark:  | `vlc`              |                           | autotools                 |
| :white_check_mark:  | `wallpaperdownloader`| [wallpaperdownloader][wallpaperdownloader] | maven  |
| :white_check_mark:  | `youtube-dl`       |                           | autotools, python3        |
[atom]: https://uappexplorer.com/app/atom-cwayne.cwayne18
[click-parser]: https://uappexplorer.com/app/click-parser.bhdouglass
[jtiledownloader]: https://uappexplorer.com/app/jtiledownloader.ogra
[keepassx-elopio]: https://uappexplorer.com/app/keepassx-elopio.elopio
[kpcli]: https://uappexplorer.com/app/kpcli-elopio.elopio
[moon-buggy]: https://uappexplorer.com/app/moon-buggy.dholbach
[qownnotes]: https://uappexplorer.com/app/qownnotes.pbek
[clock]: https://uappexplorer.com/app/ubuntu-clock-app.ubuntucoredev
[vault]: https://uappexplorer.com/app/kpcli-elopio.elopio
[wallpaperdownloader]: https://uappexplorer.com/app/wallpaperdownloader.egarcia


If the apps is listed in the second column, you can easily install it from the
store by just running: `sudo snap install <snap name>`.

## Why?

As `snapd` and its underlying technologies are new and we want to figure the
best use of it together, we want to create a space, where we collectively

 - collaborate on creating snaps
 - demonstrate best-practices
 - provide an incubator for new projects to be snapped

This is the snappy playpen.


## How it all works

No matter if you

 - are involved with an upstream project who wants to get their software snapped
 - are somebody who is interested in providing a snap for an app
 - are working on a device which needs its software snapped
 - are somebody who's curious about technology
 - think this is interesting

we want you to get involved.

### Fixing issues

If you want to provide a fix for one of the apps in this repository, simply
follow [our contributor guidelines][guidelines] and file a pull request.

### Adding new snaps

If you are working on a new, interesting snap and

 - got it working: follow the [guidelines][guidelines] and file a pull request
 - need help to get it working: send a mail to the
   [snapcraft mailing list][ml], introduce the project and push up a branch
   of your playpen fork to github, so others can take a look and help out

### Events

Over time we want to have "sprints", in which we focus on a certain piece of
software, or where we invite interested upstream developers. We are going to
announce these on the [snapcraft mailing list][ml].

## Snapping your software

The best place to get started with `snapd` and `snapcraft` is on the
[Developer Portal][devportal]. Check out the examples, and simply by running
`snapcraft init` you should be on the way to creating your first snap.

In the beginning it is a good idea to use

```yaml
confinement: devmode
```

in your `snapcraft.yaml` declaration. It will relax the security requirements
so you can get your snap fully working first and then look into the
[security bits][security] next. Just set the `confinement` value to `strict`
when you are done.

If you are collaborating with a team of developers on your snap, you might
want to run your snap build using `snapcraft cleanbuild` once you're happy with
everything. It will make sure that the build also passes in a clean container.
This way you will avoid surprises about missing `build-packages` and other
local modifications.

Once everything is fully working, consider asking the upstream project to add
your `snapcraft.yaml` file to their repository. Publishing to the store is
easy. Maybe they are going to be interested in knowing that that for every new
release or milestone, a [new snap in the store][publish] is only a matter of
running `snapcraft upload`.


## Getting in touch

If you have questions or want to get to know the people behind `snapd` and
friends, there are many ways to get in touch:

 - We are on [gitter][gitter]. Just hit us up there, it's easy.
 - There is also the [snapcraft mailing list][ml].
 - If you are on IRC, we are on `#snappy` [irc channel on Freenode][irc].

Get in touch and talk to us!

Find more support resources on the [Developer Portal][support].

[guidelines]: https://github.com/ubuntu/snappy-playpen/blob/master/CONTRIBUTING.md
[ml]: https://lists.ubuntu.com/mailman/listinfo/snapcraft
[irc]: http://webchat.freenode.net/?channels=snappy
[devportal]: https://developer.ubuntu.com/desktop
[security]: https://developer.ubuntu.com/en/snappy/guides/security/
[support]: https://developer.ubuntu.com/en/snappy/support/
[gitter]: https://gitter.im/ubuntu/snappy-playpen
[publish]: https://developer.ubuntu.com/en/snappy/build-apps/upload-your-snap/
