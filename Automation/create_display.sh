#!/bin/bash

# Generate modeline for 800x600 resolution at 60 Hz using gtf
MODELINE=$(gtf 800 480 60 | grep Modeline | cut -d ' ' -f 4-)

# Remove quotes from the mode line
MODELINE=$(echo $MODELINE | sed 's/"//g')

# Create the new mode
xrandr --newmode $MODELINE

# Extract mode name from the generated modeline
MODE_NAME=$(echo $MODELINE | cut -d ' ' -f 1)

# Prompt the user to enter the output identifier
echo "Please enter the output identifier (e.g., HDMI-0, VGA-1):"
read OUTPUT

# Add the new mode to the specified output
xrandr --addmode $OUTPUT $MODE_NAME