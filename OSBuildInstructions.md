# OS
Build Description and Documentation

## 1. Initial Setup
### 1.1 Clone the repository
```bash
git clone https://github.com/Electric-Go-Kart/OS.git
```
### 1.2 Install the required packages
```bash
~/OS/Automation/initial-setup.sh
```
## 2. Setup simulation environment (skip if not using simulation)
```bash
~/OS/Automation/CAN/vcan-setup.sh
```
### 2.1 Change the resolution mirrored to the RPi offical 7" touchscreen
To set the resolution on a Raspberry Pi to 800x480, you'll typically need to modify the configuration file for the display settings. Here's how you can do it (or you can use the `~/OS/Automation/configure_display.sh` script):

1. Open the terminal on your Raspberry Pi.
2. Edit the configuration file for the display settings by running the following command:
   ```
   sudo nano /boot/firmware/config.txt
   ```
3. Scroll down or search for the section that contains display settings.
4. Add or modify the following lines in the configuration file:
   ```
   hdmi_group=2
   hdmi_mode=87
   hdmi_cvt 800 480 60 6 0 0 0
   ```
   This configures HDMI to output 800x480 resolution at 60Hz.
5. Save your changes by pressing `Ctrl + O`, then press `Enter`. Exit the editor by pressing `Ctrl + X`.
6. Reboot your Raspberry Pi for the changes to take effect:
   ```
   sudo reboot
   ```

After rebooting, your Raspberry Pi should display at a resolution of 800x480 pixels, just like the official 7" touchscreen.

Now you are ready to develop in a virtual environment in python.

> This is needed to avoid apt package conflicts

Do so by running the following command:
```bash
source ~/gokart-env/bin/activate
```
To exit the virtual environment, run the following command (but don't do that for development):
```bash
deactivate
```

## 3. APDde setup
### 3.1 Install the required packages (ensure you're in the virtual environment)
```bash
python ~/depthai-python/examples/install_requirements.py
```
Clone the repository:
```bash
cd ~/projects
git clone https://github.com/Electric-Go-Kart/APDde.git
```

### 3.2 Run the APDde with the OAK-D Pro connected
```bash
~/projects/APDde/APDde.py
```

## 4. User Interface Setup
### 4.1 Clone the repository and any further repositories in the ~/projects directory

This is where the EKart software lives:
```bash
cd ~/projects
```

So in that directory:
```bash
git clone https://github.com/Electric-Go-Kart/EKartUI.git
```
### 4.2 
```bash
cd ~/projects/EKartUI
git checkout spencer
```

### 4.3 Install the required packages
```bash
pip install -r requirements.txt
```
### 4.4 Run the UI
```bash
./start_ui.sh
```
> If you are not in simulation, you will need to run the steps in section 5 to setup the CAN interface

## 5. GPS Setup (Not verified yet)
### 5.1 Clone
```bash
git clone https://github.com/Electric-Go-Kart/GPS
```
### 5.2 Install the required packages
```bash
sudo apt install gpsd gpsd-clients -y
```
### 5.3 Run the GPS (verify installation)
```bash
cgps -s
```

### 6. CAN Setup is under the ~/OS/Automation/CAN directory