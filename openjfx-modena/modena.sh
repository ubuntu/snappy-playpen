#!/bin/sh
export JAVA_HOME=$SNAP/usr/lib/jvm/java-8-openjdk-amd64
export PATH=$JAVA_HOME/jre/bin:$PATH

java -jar $SNAP/Modena.jar
