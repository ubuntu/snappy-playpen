#!/bin/sh
echo "starting gogs"
export USERNAME=root
export USER=root

echo "running as user ${USERNAME}"

if [ -e $SNAP_COMMON/app.ini ]; then
  echo "configuration already present"
else
  echo "configuration points to ${SNAP_COMMON}"
  cp $SNAP/app.ini $SNAP_COMMON/app.ini
  cp -r $SNAP/templates $SNAP_COMMON/templates
  cp -r $SNAP/scripts $SNAP_COMMON/scripts
  cp -r $SNAP/public $SNAP_COMMON/public
fi
exec $SNAP/bin/gogs web -c $SNAP_COMMON/app.ini -p 3001
