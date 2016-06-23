# -*- Mode:Makefile; indent-tabs-mode:t; tab-width:4 -*-

TMPDIR= ./unpack
OPT = $(TMPDIR)/opt/Gitter/linux64
OUTDIR = ../src/
VERSION = $(shell sed -n -e "s/\"//g" -e "s/-.*$$//; s/^[^=]*version[^:]*:[[:blank:]]*//p" ../src/snapcraft.yaml )
URL = http://update.gitter.im/linux64

all: clean download

install:
	mkdir -p $(OUTDIR)setup/gui
	sed "s/^Icon=.*/Icon=$$\{SNAP\}\/meta\/gui\/icon.png/; s/^Exec=.*/Exec=gitter/g" $(OPT)/gitter.desktop >$(OUTDIR)setup/gui/gitter.desktop
	mv $(OPT)/Gitter $(OUTDIR)
	mv $(OPT)/icudtl.dat $(OUTDIR)
	mv $(OPT)/libffmpegsumo.so $(OUTDIR)
	mv $(OPT)/locales $(OUTDIR)
	mv $(OPT)/nw.pak $(OUTDIR)
	mv $(OPT)/logo.png $(OUTDIR)setup/gui/icon.png
	rm -rf *.deb
	rm -rf $(TMPDIR)

download:
	wget $(URL)/gitter_$(VERSION)_amd64.deb
	dpkg -x gitter_$(VERSION)_amd64.deb $(TMPDIR)

clean:
	rm -f Gitter
	rm -f icudtl.dat
	rm -f libffmpegsumo.so
	rm -rf locales
	rm -f nw.pak
	rm -rf setup
