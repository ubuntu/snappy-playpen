#! /bin/sh

PORT=8080
TIMEOUT=600
ERRFILE="$SNAP/usr/share/tinyproxy/default.html"
STATFILE="$SNAP/usr/share/tinyproxy/stats.html"
LOGFILE="$SNAP_DATA/tinyproxy.log"
FILTERFILE="$SNAP_DATA/filter"
PIDFILE="$SNAP_DATA/tinyproxy.pid"

if [ ! -e $SNAP_DATA/tinyproxy.conf ]; then
    sed -e "s;^Port [0-9]*;Port $PORT;"\
        -e "s;^User .*;#User nobody;"\
        -e "s;^Group .*;#Group nogroup;"\
        -e "s;^Timeout [0-9]*;Timeout $TIMEOUT;"\
        -e "s;^DefaultErrorFile .*;DefaultErrorFile \"${ERRFILE}\";"\
        -e "s;^StatFile .*;StatFile \"$STATFILE\";"\
        -e "s;^Logfile .*;Logfile \"$LOGFILE\";"\
        -e "s;^#Filter .*;Filter \"$FILTERFILE\";"\
        -e "s;^PidFile .*;PidFile \"$PIDFILE\";" $SNAP/etc/tinyproxy.conf >$SNAP_DATA/tinyproxy.conf
    touch $SNAP_DATA/filter
fi

exec $SNAP/usr/sbin/tinyproxy -d -c $SNAP_DATA/tinyproxy.conf
