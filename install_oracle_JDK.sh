#!/bin/zsh
# Java install script
# Requirement: Downlaod Oracle JDK into ~/Downloads/
# Note: Run this script with `sudo`
# Note: Run `:%s/131/$VERSION_NUM/g to replace the sub-version number to  what you actually downloaded
#
cd /usr/local
mkdir java
cd java
tar zxvf  ~/Downloads/jdk-8u131-linux-x64.tar.gz 
#x: extract, z: for unzipping gz, v: verbose, f: filename

update-alternatives --install "/usr/bin/java" "java" "/usr/local/java/jdk1.8.0_131/jre/bin/java" 1
# --install symlink name path priority
update-alternatives --install "/usr/bin/javac" "javac" "/usr/local/java/jdk1.8.0_131/bin/javac" 1
update-alternatives --install "/usr/bin/javaws" "javaws" "/usr/local/java/jdk1.8.0_131/jre/bin/javaws" 1

# Use this Oracle JDK/JRE as the default
update-alternatives --set java /usr/local/java/jdk1.8.0_131/jre/bin/java
# --set name path
update-alternatives --set javac /usr/local/java/jdk1.8.0_131/bin/javac
update-alternatives --set javaws /usr/local/java/jdk1.8.0_131/jre/bin/javaws

# Verify 
ls -ld /usr/bin/java*
ls -ld /etc/alternatives/java*

javac -version
java -version

which javac
which java

