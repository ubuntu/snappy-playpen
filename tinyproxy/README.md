The proxy runs on port 8080 and only allows connections from localhost by default.
If you want to make it usable network wide edit:

/var/snap/tinyproxy/current/tinyproxy.conf

and restart the service with:

sudo systemctl restart snap.tinyproxy.tinyprox

To define filter rules for blocked urls you can edit:

/var/snap/tinyproxy/current/filter

and just add domain names or full url paths (you do not need http://)
to that file and they will be blocked.

To make the new filters used you need to restart the proxy again with:

sudo systemctl restart snap.tinyproxy.tinyprox

Logs are written to:

/var/snap/tinyproxy/current/tinyproxy.log
