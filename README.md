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
~/OS/Automation/can-setup.sh
```
## 2.1 Change the resolution mirrored to the RPi offical 7" touchscreen
```bash:
To set the resolution on a Raspberry Pi to 800x480, you'll typically need to modify the configuration file for the display settings. Here's how you can do it:

1. Open the terminal on your Raspberry Pi.
2. Edit the configuration file for the display settings by running the following command:
   ```
   sudo nano /boot/config.txt
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

After rebooting, your Raspberry Pi should display at a resolution of 800x480.