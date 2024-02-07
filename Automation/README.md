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
```bash
~/OS/Automation/can-setup.sh
```
Verify the can bus is enabled by running the following command:
```bash
ifconfig can0
```
OR
```bash
ip -details -statistics link show can0
```