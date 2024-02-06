#!/bin/bash

# Define the lines to add
lines_to_add=(
    "hdmi_group=2"
    "hdmi_mode=87"
    "hdmi_cvt 800 480 60 6 0 0 0"
)

# Path to the configuration file
config_file="/boot/firmware/config.txt"

# Check if each line already exists, if not, add it
for line in "${lines_to_add[@]}"; do
    if ! grep -qF "$line" "$config_file"; then
        echo "Adding line: $line"
        echo "$line" | sudo tee -a "$config_file" > /dev/null
    else
        echo "Line already exists: $line"
    fi
done

# Prompt to reboot if changes were made
if [[ "${#lines_to_add[@]}" -gt 0 ]]; then
    echo "Changes applied. Rebooting Raspberry Pi..."
    sudo reboot
else
    echo "No changes needed. Exiting."
fi
