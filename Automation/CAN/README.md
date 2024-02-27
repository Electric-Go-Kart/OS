# Virtual CAN Bus
To run virtual can bus, you need to install the following packages:
```bash
sudo apt-get install can-utils
```
To enable the virtual can bus, run the following command:
```bash
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
```
To send random data on the virtual can bus, run the following command:
```bash
cangen vcan0
```
To receive data on the virtual can bus, run the following command:
```bash
candump vcan0
```
To run simultaneous send and receive on the virtual can bus, run the following command:
```bash
cangen vcan0 | candump vcan0
```
To run the virtual can bus piped to the python script, run the following command:
```bash
cangen vcan0 | python3 ~/projects/EKartUI/can_parse.py
```
Then follow the instructions in EKartUI

# CAN Bus
To enable the can bus, run the following command:

Load the required kernel modules:
```bash
sudo modprobe can
sudo modprobe can_raw
sudo modprobe can_dev
```

> Make sure you are specifying the GPIO as the GPIO # not the PIN HEADER for this command:
```bash
~/OS/Automation/can-setup.sh
```
Set up the can bus by running the following command:
```bash
sudo ip link set can0 up type can bitrate 500000
```

If this doesn't work, ensure that the correct interrupt is defined in config.txt or run the following commands to debug the situation:
```bash
lsmod | grep can
```
```bash
lsmod | grep spi
```
```bash
dmesg | grep spi
```
```bash
dmesg | grep can
```
```bash
dmesg | grep mcp
```


Verify the can bus is enabled by running the following command:
```bash
ifconfig can0
```
OR
```bash
ip -details -statistics link show can0
```
Documentation: https://forums.raspberrypi.com/viewtopic.php?t=141052

# Ensure the can bus is enabled on boot
To ensure the can bus is enabled on boot, run the following command:
```bash
sudo nano /etc/network/interfaces
```
Add the following lines to the file:
```bash
auto can0
iface can0 can static
    bitrate 500000
```
Then reboot the system:
```bash
sudo reboot
```
