#!/bin/bash
ANSWER=$(echo -e "\n\n󰗼" | rofi -config ~/.config/qtile/config.rasi.qtile.power -no-fixed-num-lines -dmenu)
if [ "$ANSWER" = "" ]; then
systemctl poweroff
elif [ "$ANSWER" = "" ]; then
systemctl reboot
elif [ "$ANSWER" = "󰗼" ]; then
qtile cmd-obj -o cmd -f shutdown 
fi
