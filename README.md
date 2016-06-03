# snappy playpen

A place to test snapcraft, learn creating snaps and share best practices.

Get started here: http://developer.ubuntu.com/desktop

## Current project health
[![Build Status](https://api.travis-ci.org/ubuntu/snappy-playpen.svg?branch=master)](https://travis-ci.org/ubuntu/snappy-playpen) (snapcraft and snappy playpen health check)

## Why?

As `snapd` and its underlying technologies are new and we want to figure the
best use of it together, we want to create a space, where we collectively

 - collaborate on creating snaps
 - demonstrate best-practices
 - provide an incubator for new projects to be snapped

This is snappy playpen.


## How it all works

No matter if you

 - are involved with an upstream project who wants to get their software snapped
 - are somebody who is interested in providing a snap for an app
 - are working on a device which needs its software snapped
 - are somebody who's curious about technology
 - think this is interesting

we want you to get inolved.

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
confinement: devmode```
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
`snapcraft upload`.


## Getting in touch

There's obviously the [snapcraft mailing list][ml], but there's also the
`#snappy` [irc channel on Freenode][irc]. Get in touch and talk to us!

Find more support resources on the [Developer Portal][support].

[guidelines]: https://github.com/ubuntu/snappy-playpen/blob/master/CONTRIBUTING.md
[ml]: https://lists.ubuntu.com/mailman/listinfo/snapcraft
[irc]: http://webchat.freenode.net/?channels=snappy
[devportal]: https://developer.ubuntu.com/desktop
[security]: https://developer.ubuntu.com/en/snappy/guides/security/
[support]: https://developer.ubuntu.com/en/snappy/support/
[publish]: https://developer.ubuntu.com/en/snappy/build-apps/upload-your-snap/
