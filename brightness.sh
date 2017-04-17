[[ $# -eq 0 ]] && {
	cat /sys/class/backlight/panel/actual_brightness
}
[[ $# -gt 0 ]] && {
	brightness=$1
	[[ $1 == [0-9]* ]] || {
		brightness=$(</sys/class/backlight/panel/actual_brightness)
		[[ "$1" == "-" ]] && {
			let "brightness-=16"
		}
		[[ "$1" == "+" ]] && {
			let "brightness+=16"
		}
	}
	[[ "$brightness" -lt 0 ]]   && brightness=0
	[[ "$brightness" -gt 255 ]] && brightness=255
	echo $brightness > /sys/class/backlight/panel/brightness
}
