#!/bin/bash

# Ensure the can-utils package is installed
sudo apt install can-utils -y
sudo modprobe can
sudo modprobe can_raw

# User inputs the GPIO pin number for the CAN interrupt
echo "Enter the GPIO pin number for the CAN interrupt: "
read interrupt

# Add or modify the dtoverlay line in the config.txt file
sed -i '/dtoverlay=mcp2515-can0/d' /boot/firmware/config.txt
echo "dtoverlay=mcp2515-can0,oscillator=10000000,interrupt=$interrupt" >> /boot/firmware/config.txt

# Check if permission denied error occurs
if [ $? -ne 0 ]; then
    echo "Permission denied error. Please run the script with sudo."
    exit 1
fi

# Reboot the Raspberry Pi to apply the changes
echo "Changes applied. Rebooting Raspberry Pi and check /boot/firmware/config.txt..."
sleep 3
sudo reboot