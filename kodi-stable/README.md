# Kodi snap

This project creates a working snap of Kodi 16.1-Jarvis.

## Current state

Working features:
 - Play any video works.
 - Video plugins.
 - Hardware decode works.
 - Skins and fonts.
 - Images.

Known issues:
  - The home folder is empty because its not the real one, you should explore from "/".
  - Only works in devmode because the following access problems:
  
  Jul 18 21:35:49 XXXXXXXX kernel: [ 5027.853512] audit: type=1107 audit(1468895749.317:2879): pid=886 uid=106 auid=4294967295 ses=4294967295 msg='apparmor="ALLOWED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/UPower" interface="org.freedesktop.UPower" member="EnumerateDevices" mask="send" name="org.freedesktop.UPower" pid=10058 label="snap.kodi.kodi" peer_pid=1500 peer_label="unconfined"
Jul 18 21:35:49 XXXXXXXX kernel: [ 5027.853512]  exe="/usr/bin/dbus-daemon" sauid=106 hostname=? addr=? terminal=?'
Jul 18 21:35:49 XXXXXXXX kernel: [ 5027.855315] audit: type=1107 audit(1468895749.317:2880): pid=886 uid=106 auid=4294967295 ses=4294967295 msg='apparmor="ALLOWED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/UPower" interface="org.freedesktop.UPower" member="EnumerateDevices" mask="send" name="org.freedesktop.UPower" pid=10058 label="snap.kodi.kodi" peer_pid=1500 peer_label="unconfined"
Jul 18 21:35:49 XXXXXXXX kernel: [ 5027.855315]  exe="/usr/bin/dbus-daemon" sauid=106 hostname=? addr=? terminal=?'
Jul 18 21:35:49 XXXXXXXX kernel: [ 5027.856093] audit: type=1107 audit(1468895749.317:2881): pid=886 uid=106 auid=4294967295 ses=4294967295 msg='apparmor="ALLOWED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="CanPowerOff" mask="send" name="org.freedesktop.login1" pid=10058 label="snap.kodi.kodi" peer_pid=903 peer_label="unconfined"
Jul 18 21:35:49 XXXXXXXX kernel: [ 5027.856093]  exe="/usr/bin/dbus-daemon" sauid=106 hostname=? addr=? terminal=?'
Jul 18 21:35:49 XXXXXXXX kernel: [ 5027.860905] audit: type=1107 audit(1468895749.325:2882): pid=886 uid=106 auid=4294967295 ses=4294967295 msg='apparmor="ALLOWED" operation="dbus_method_call"  bus="system" path="/org/freedesktop/login1" interface="org.freedesktop.login1.Manager" member="CanReboot" mask="send" name="org.freedesktop.login1" pid=10058 label="snap.kodi.kodi" peer_pid=903 peer_label="unconfined"
Jul 18 21:35:49 XXXXXXXX kernel: [ 5027.860905]  exe="/usr/bin/dbus-daemon" sauid=106 hostname=? addr=? terminal=?'

TODO:
 - More testing.
 
