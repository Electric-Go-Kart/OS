#!/bin/bash
# Prompt the user to enter the output identifier
echo "Please enter the output identifier (e.g., HDMI-0, VGA-1):"
read OUTPUT

# Prompt the user to select the mode
echo "Please enter the mode you wish to set (e.g., 800x480_60.00):"
read SELECTED_MODE

# Change the display to the selected resolution
xrandr --output $OUTPUT --mode $SELECTED_MODE