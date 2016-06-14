define NPM_CONF
global = true
unsafe-perm = true
endef
export NPM_CONF

define ETHERPAD_CONF
/*
  This file must be valid JSON. But comments are allowed

  See https://github.com/ether/etherpad-lite/blob/develop/settings.json.template
  to learn about the meaning of eadh

*/
{
  "title": "Etherpad",
  "favicon": "favicon.ico",
  "ip": "127.0.0.1",
  "port" : 9001,
  "dbType" : "dirty",
	/* This is pretty much a hack for now*/
  "dbSettings" : {
                   "filename" : "/var/snap/etherpad-lite-unofficial/current/dirty.db"
                 },
  "defaultPadText" : "Welcome to Etherpad!\n\nThis pad text is synchronized as you type, so that everyone viewing this page sees the same text. This allows you to collaborate seamlessly on documents!\n\nGet involved with Etherpad at http:\/\/etherpad.org\n",
  "padOptions": {
    "noColors": false,
    "showControls": true,
    "showChat": true,
    "showLineNumbers": true,
    "useMonospaceFont": false,
    "userName": false,
    "userColor": false,
    "rtl": false,
    "alwaysShowChat": false,
    "chatAndUsers": false,
    "lang": "en-gb"
  },
  "suppressErrorsInPadText" : false,
  "requireSession" : false,
  "editOnly" : false,
  "sessionNoPassword" : false,
  "minify" : true,
  "maxAge" : 21600,
  "abiword" : null,
  "soffice" : null,
  "tidyHtml" : null,
  "allowUnknownFileEnds" : true,
  "requireAuthentication" : false,
  "requireAuthorization" : false,
  "trustProxy" : false,
  "disableIPlogging" : false,
  "users": {
    "admin": {
      "password": "changeme1",
      "is_admin": true
    },
    "user": {
      "password": "changeme1",
      "is_admin": false
    }
  },
  "socketTransportProtocols" : ["xhr-polling", "jsonp-polling", "htmlfile"],
  "loadTest": false,
  "loglevel": "INFO",
  "logconfig" :
    { "appenders": [
        { "type": "console"
        }
      ]
    }
}
endef
export ETHERPAD_CONF

all:

build:
	@echo "$$NPM_CONF" > npmrc
	@echo "$$ETHERPAD_CONF" > settings.json

install: build
	install -D -m644 npmrc $(DESTDIR)/etc/npmrc
	install -D -m644 settings.json $(DESTDIR)/etc/settings.json
	install -D -m755 runpad $(DESTDIR)/bin/runpad
