FROM ubuntu:xenial

RUN apt update && apt dist-upgrade -y && apt install -y git && apt clean

# enable multiverse as snapcraft cleanbuild does.
RUN sed -i 's/ universe/ universe multiverse/' /etc/apt/sources.list

# build and install snapcraft from master.
git clone https://github.com/snapcore/snapcraft
cd snapcraft
apt build-dep -y ./
dpkg-buildpackage -us -uc
apt install ../*.deb
