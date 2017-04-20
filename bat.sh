#!/bin/sh

charge=$(</sys/class/power_supply/battery/charge_now)
capacity=$(</sys/class/power_supply/battery/capacity)
case $1 in
  "status")
    [[ $charge -gt 0 ]] && echo charging
    [[ $charge -gt 0 ]] || echo discharging
    ;;
  "percent")
    echo $capacity
    ;;
  *)
    res="$capacity%"
    [[ $charge -gt 0 && $capacity -ne 100 ]] && res="+$res"
    echo $res
esac
