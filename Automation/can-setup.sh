#!/bin/bash

# Load the can-utils module
sudo apt install can-utils -y

# Create a virtual CAN interface
sudo ip link add dev vcan0 type vcan

# Bring up the virtual CAN interface
sudo ip link set up vcan0

# Start the can-utils candump tool to monitor the CAN traffic
candump vcan0
