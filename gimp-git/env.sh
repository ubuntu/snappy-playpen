#!/bin/sh

ARCH='x86_64-linux-gnu'

export LD_LIBRARY_PATH=$SNAP/lib:$LD_LIBRARY_PATH
export XDG_DATA_DIRS=$SNAP/share:$XDG_DATA_DIRS
export ACLOCAL_FLAGS="-I $SNAP/share/aclocal"
export PKG_CONFIG_PATH=$SNAP/lib/pkgconfig:$PKG_CONFIG_PATH
export GIO_EXTRA_MODULES=/usr/lib/$ARCH/gio/modules

mkdir ./parts/lib 
mkdir ./parts/lib/pkgconfig 
mkdir ./parts/share 
mkdir ./parts/share/aclocal

snapcraft
