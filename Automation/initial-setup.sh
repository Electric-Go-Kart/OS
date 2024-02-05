#!/bin/bash -e

# This script configures the gokart image
# 1. Update and Upgrade the system
sudo apt-get update && sudo apt-get upgrade -y

# 3. Configure SSH, VNC, and SPI
# 3.1. Enable SSH
sudo raspi-config nonint do_ssh 0

# 3.2. Enable wayland for VNC
sudo raspi-config nonint do_vnc 0

# 3.3. Enable SPI
sudo raspi-config nonint do_spi 0

# Make project directory
mkdir -p ~/projects
cd ~/projects

# Create a virtual environment in the home directory
python3 -m venv ~/gokart-env

# 4. Reboot the system
echo "Rebooting the system..."
sudo reboot