export JAVA_HOME=$SNAP/usr/lib/jvm/java-8-openjdk-amd64
export PATH=$JAVA_HOME/jre/bin:$PATH

# Not good, needed for fontconfig
export XDG_DATA_HOME=$SNAP/usr/share
# Font Config
export FONTCONFIG_PATH=$SNAP/etc/fonts/config.d
export FONTCONFIG_FILE=$SNAP/etc/fonts/fonts.conf
java -jar -Duser.home=$SNAP_USER_DATA $SNAP/usr/share/doc/openjdk-8-demo/demo/jfc/FileChooserDemo/FileChooserDemo.jar
