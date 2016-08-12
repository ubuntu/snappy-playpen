FROM ubuntu:xenial

RUN apt-get update && apt-get dist-upgrade -y && apt-get install -y devscripts equivs git

# enable multiverse as snapcraft cleanbuild does.
RUN sed -i 's/ universe/ universe multiverse/' /etc/apt/sources.list

# build and install snapcraft from master.
RUN git clone https://github.com/snapcore/snapcraft && \
  cd snapcraft && \
  mk-build-deps debian/control -i --tool 'apt-get -y' && \
  dpkg-buildpackage -us -uc && \
  apt-get install -y ../*.deb && \
  apt-get clean -y && \
  apt-get remove --purge -y devscripts equivs git python3-fixtures python3-responses python3-setuptools python3-testscenarios python3-testtools && \
  apt-get autoremove -y
