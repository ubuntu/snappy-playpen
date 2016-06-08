# TinyProxy snap

The proxy runs on port 8080 and only allows connections from localhost by default.

## Configuration

If you want to change the configuartion edit:

/var/snap/tinyproxy/current/tinyproxy.conf

and restart the service with:

sudo systemctl restart snap.tinyproxy.tinyproxy

## URL blocking/filtering

To define filter rules for blocked urls you can edit:

/var/snap/tinyproxy/current/filter

and just add domain names or full url paths (you do not need http://)
to that file and they will be blocked.

To make the new filters used you need to restart the proxy again with:

sudo systemctl restart snap.tinyproxy.tinyproxy

## Logging

Logs are written to:

/var/snap/tinyproxy/current/tinyproxy.log
