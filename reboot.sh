#!/bin/sh

sudo rm -rf /tmp/*
sync
unchroot reboot -d 8 -f
