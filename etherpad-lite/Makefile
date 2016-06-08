define NPM_CONF
global = true
unsafe-perm = true
endef
export NPM_CONF

all:

build:
	@echo "$$NPM_CONF" > npmrc

install: build
	install -D -m644 npmrc $(DESTDIR)/etc/npmrc
	install -D -m755 runpad $(DESTDIR)/bin/runpad
