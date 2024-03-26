#!/bin/bash

# Config lines to add
config_lines="# For 180 degree rotation (upside down)
display_lcd_rotate=2
dtoverlay=rpi-ft5406,touchscreen-inverted-x=1,touchscreen-inverted-y=1"

# Append lines to config.txt
echo "$config_lines" | sudo tee -a /boot/firmware/config.txt > /dev/null

echo "Lines added to /boot/firmware/config.txt"
