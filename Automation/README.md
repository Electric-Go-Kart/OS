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
Then follow the instructions for the README under EKartUI