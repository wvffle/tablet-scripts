#!/bin/sh

sudo rm -rf /tmp/*
sync
unchroot reboot -f
