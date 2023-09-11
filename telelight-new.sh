#! /bin/bash

delay="2s"
regex=Telegram\ .*
altered=0
echo \* Telegram ThinkLight notifications \* 


while true; do
    if [[ $(cat /sys/class/leds/tpacpi\:\:thinklight/brightness) == 0 ]]
    then
		newmsg=$(xdotool search --onlyvisible --class Telegram | xargs -I % xdotool getwindowname %)
		if [[ "$newmsg" =~ Telegram\ .* ]]
			then
				altered=1
				echo 255 > /sys/class/leds/tpacpi\:\:thinklight/brightness
		fi	
	elif [[ $(cat /sys/class/leds/tpacpi\:\:thinklight/brightness) == 255 && $altered == 1 ]]
	then
		newmsg=$(xdotool search --onlyvisible --class Telegram | xargs -I % xdotool getwindowname %)
		if [[ "$newmsg" == $'Telegram\nTelegram' ]]
			then
				altered=0
				echo 0 > /sys/class/leds/tpacpi\:\:thinklight/brightness
		fi
    fi
    sleep $delay
done