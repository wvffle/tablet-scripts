#!/bin/sh

cat /dev/zero > /dev/graphics/fb0
sudo rm -rf /tmp/*
sync
unchroot reboot -d 8 -f
