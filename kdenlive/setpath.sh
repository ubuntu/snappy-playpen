#!/bin/sh

echo "starting script\n"
export PATH="$SNAP/usr/bin:$PATH"
export LADSPA_PATH="$SNAP/usr/lib/ladspa"
export MLT_DATA="$SNAP/usr/share/mlt/"
export MLT_PROFILES_PATH="$SNAP/usr/share/mlt/profiles"
export MLT_PRESETS_PATH="$SNAP/usr/share/mlt/presets"
export MLT_REPOSITORY="$SNAP/usr/lib/mlt/"
export LD_LIBRARY_PATH="$SNAP/usr/lib/x86_64-linux-gnu/:$LD_LIBRARY_PATH"
export LD_LIBRARY_PATH="$SNAP/usr/lib/x86_64-linux-gnu/alsa-lib:$LD_LIBRARY_PATH"
export LD_LIBRARY_PATH="$SNAP/usr/lib/x86_64-linux-gnu/dri:$SNAP/usr/lib/x86_64-linux-gnu/qt5/lib:$LD_LIBRARY_PATH"
export LIBGL_DRIVERS_PATH="$SNAP/usr/lib/x86_64-linux-gnu/dri"

export FREI0R_PATH="$SNAP/usr/lib/frei0r-1"
export MLT_MOVIT_PATH="$SNAP/usr/share/movit"
export QT_PLUGIN_PATH="$SNAP/usr/lib/x86_64-linux-gnu/qt5/plugins"
export QML2_IMPORT_PATH="$SNAP/usr/lib/x86_64-linux-gnu/qt5/qml"
export DESKTOP_SESSION=ubuntu
export XDG_SESSION_DESKTOP=ubuntu
export XDG_CURRENT_DESKTOP=kde
export XDG_CONFIG_DIRS=$SNAP/etc:$XDG_CONFIG_DIRS
export XDG_DATA_DIRS=$SNAP/usr/share:$XDG_DATA_DIRS
export QT_QPA_PLATFORMTHEME=appmenu-qt5
export LOCPATH=$SNAP/usr/lib/locale

# Set cache folder to local path, dependent on snap version
export XDG_CACHE_HOME=$SNAP_USER_DATA/.cache-$SNAP_VERSION
mkdir -p $XDG_CACHE_HOME

echo $SNAP
cd $SNAP
#echo "testing MLT --------------------\n"
#melt color:red out=200 -consumer xgl
echo "testing kdenlive --------------------\n"
desktop-launch $SNAP/usr/bin/kdenlive
