#!/bin/sh

while [ 1 -eq 1 ]
do
  sleep 1
  [[ $(ps -u|grep -ci xinit\ --) -lt 2 ]] && xinit -- :0 -dpi 100 -sharevts vt0&
done
