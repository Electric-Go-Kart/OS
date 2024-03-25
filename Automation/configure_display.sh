#!/bin/bash

# Generate modeline for 800x480 resolution at 60 Hz
MODELINE=$(cvt 800 480 60 | grep Modeline | cut -d ' ' -f 2-)

# Create the new mode
xrandr --newmode $MODELINE

# Prompt the user to enter the output identifier
echo "Please enter the output identifier (e.g., HDMI-0, VGA-1):"
read OUTPUT

# Add the new mode to the specified output
xrandr --addmode $OUTPUT 800x480