# DEPRECATED - The snappy playpen

This project is not updated any more. Good examples should be moved to

 * http://snapcraft.io
 * https://github.com/snapcore/snapcraft

## Project status

The Snappy Playpen used to be place, where we learned from each other and documented best-practices. This was useful in the very first days of `snapcraft`, but after more and more discussions we realised that it's time to merge the best examples into the [snapcraft code](https://github.com/snapcore/snapcraft) itself. This is where most eyeballs go.

## Learning

If you are new and want to get started, check out the docs here:
 * [Get started >](http://snapcraft.io)
 * [Basic snap and snapcraft notions >](http://snapcraft.io/create/)

## Contributing examples

If you feel you created a great example and want to get it included somewhere, bring it up on the [snapcraft mailing list][ml].

## Current project status
This project currently includes the following snaps:

| State               | App                | Snap name in the store    | Uses                      |
| ------------------- | ------------------ | ------------------------- | ------------------------- |
| :white_check_mark:  | `2048`             |                           | qt5, qml, dump            |
| :white_check_mark:  | `atom`             | [atom-cwayne][atom]       | electron, grunt, nodejs   |
| :white_check_mark:  | `baka-mplayer`     |                           | qt5, qml, mpv             |
| :white_check_mark:  | `cloudfoundry-cli` |                           | go                        |
| :white_check_mark:  | `consul`           | [consul][consul]          | go                        |
| :white_check_mark:  | `click-parser`     | [click-parser][click-parser] | nodejs                 |
| :white_check_mark:  | `cuberite    `     |                           | cmake                     |
| :white_check_mark:  | `dcos-cli`         |                           | python3                   |
| :red_circle:        | `deis-workflow-cli`|                           | go                        |
| :white_check_mark:  | `dekko`            |                           | qt5, qml, dump, oxide, cmake |
| :white_check_mark:  | `dosbox`           |                           | autotools                 |
| :white_check_mark:  | `docker-compose`   |                           | python3                   |
| :white_check_mark:  | `ffmpeg`           |                           | autotools                 |
| :white_check_mark:  | `galculator`       |                           | autotools, gtk3           |
| :white_check_mark:  | `gitter-im`        |                           | copy, gtk3, wget          |
| :white_check_mark:  | `grive    `        |                           | cmake                     |
| :white_check_mark:  | `gogs     `        |                           | go,dump, copy             |
| :white_check_mark:  | `hellogl  `        |                           | cmake, opengl             |
| :white_check_mark:  | `hellomako`        |                           | python                    |
| :white_check_mark:  | `healthcheck-toolbox interface` | [healthcheck-toolbox-example][healthcheck-toolbox-example] | dump |
| :red_circle:        | `heroku`           |                           | go                        |
| :white_check_mark:  | `hexchat`          | [unofficial-hexchat][unofficial-hexchat] | autotools, gtk2, perl, python2, lua |
| :white_check_mark:  | `idea`             |                           | ant, antIntellij, java, openjdk |
| :white_check_mark:  | `imagemagick6-stable`|                         | autotools                 |
| :red_circle:        | `imagemagick7-git` |                           | autotools                 |
| :white_check_mark:  | `jtiledownloader`  | [jtiledownloader][]       | dump, jar, java           |
| :white_check_mark:  | `keepassx`         | [keepassx-elopio][]       | cmake, qt5                |
| :white_check_mark:  | `kdenlive`         |                           | cmake, qt5, opengl        |
| :white_check_mark:  | `kpcli`            | [kpcli-elopio][kpcli]     | dump, perl                |
| :white_check_mark:  | `kodi-stable`      |                           | autotools                 |
| :white_check_mark:  | `leafpad`          |                           | autotools, gtk2, lubuntu, xubuntu |
| :white_check_mark:  | `mesa-demos`       |                           | opengl, opengles, egl     |
| :white_check_mark:  | `minetest`         |                           | cmake, copy               |
| :white_check_mark:  | `mirageos`         |                           | caml, opam, make          |
| :white_check_mark:  | `moon-buggy`       | [moon-buggy][moon-buggy]  | curses, autotools         |
| :white_check_mark:  | `mpv`              |                           | autotools, waf            |
| :white_check_mark:  | `openjdk-demo`     |                           | java, openjdk             |
| :white_check_mark:  | `openttd`          |                           | dump, qt5                 |
| :red_circle:        | `plank`            |                           | autotools, vala           |
| :white_check_mark:  | `ps-mem`           |                           | python3                   |
| :white_check_mark:  | `qcomicbook`       |                           | cmake, qt5                |
| :red_circle:        | `qdriverstation`   |                           | frc, qmake, qt5, robotics |
| :white_check_mark:  | `qownnotes`        | [qownnotes][qownnotes]    | qmake, qt5, tar           |
| :white_check_mark:  | `residualvm`       |                           | autotools                 |
| :white_check_mark:  | `ristretto`        |                           | qmake, qt5, tar           |
| :white_check_mark:  | `scummvm`          |                           | autotools                 |
| :white_check_mark:  | `shotwell`         |                           | autotools, vala           |
| :white_check_mark:  | `smplayer`         |                           | qt5, stage-package        |
| :white_check_mark:  | `taskwarrior`      |                           | dump, cmake               |
| :white_check_mark:  | `texworks`         |                           | dump, qt4, cmake          |
| :white_check_mark:  | `timewarrior`      |                           | cmake                     |
| :white_check_mark:  | `tinyproxy`        |                           | dump, daemon, stage-package |
| :white_check_mark:  | `tyrant-unleashed-optimizer` |                 | make                      |
| :white_check_mark:  | `ubuntu-clock-app` | [ubuntu-clock-app][clock] | qmake, qt5                |
| :white_check_mark:  | `ubuntukylin-icon-theme` |                     | copy_and_edit, theme      |
| :white_check_mark:  | `vault`            | [vault-elopio][vault]     | go                        |
| :white_check_mark:  | `vlc`              |                           | autotools                 |
| :white_check_mark:  | `wallpaperdownloader`| [wallpaperdownloader][wallpaperdownloader] | maven, stage-package, snapcraft-desktop-helpers part, gsettings  |
| :white_check_mark:  | `youtube-dl`       |                           | autotools, python3        |
| :white_check_mark:  | `zsh`              |                           | autotools                 |
[atom]: https://uappexplorer.com/app/atom-cwayne.cwayne18
[click-parser]: https://uappexplorer.com/app/click-parser.bhdouglass
[unofficial-hexchat]: https://uappexplorer.com/app/unofficial-hexchat.diddledan
[jtiledownloader]: https://uappexplorer.com/app/jtiledownloader.ogra
[keepassx-elopio]: https://uappexplorer.com/app/keepassx-elopio.elopio
[kpcli]: https://uappexplorer.com/app/kpcli-elopio.elopio
[moon-buggy]: https://uappexplorer.com/app/moon-buggy.dholbach
[qownnotes]: https://uappexplorer.com/app/qownnotes.pbek
[clock]: https://uappexplorer.com/app/ubuntu-clock-app.ubuntucoredev
[vault]: https://uappexplorer.com/app/vault-elopio.elopio
[wallpaperdownloader]: https://uappexplorer.com/app/wallpaperdownloader.egarcia


If the apps is listed in the second column, you can easily install it from the
store by just running: `sudo snap install <snap name>`.



## Getting in touch

If you have questions or want to get to know the people behind `snapd` and
friends, there are many ways to get in touch:

 - We are on the [snapcraft mailing list][ml].
 - If you are on IRC, we are on `#snappy` [irc channel on Freenode][irc].

Get in touch and talk to us!

Find more support resources on the [Developer Portal][support].

[guidelines]: https://github.com/ubuntu/snappy-playpen/blob/master/CONTRIBUTING.md
[ml]: https://lists.ubuntu.com/mailman/listinfo/snapcraft
[irc]: http://webchat.freenode.net/?channels=snappy
[security]: https://developer.ubuntu.com/en/snappy/guides/security/
[support]: http://snapcraft.io/community/
[publish]: https://developer.ubuntu.com/en/snappy/build-apps/upload-your-snap/
