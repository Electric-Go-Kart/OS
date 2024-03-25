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
To set the resolution on a Raspberry Pi to 800x480, you'll typically need to modify the display settings. Here's how you can do it (or you can use the `~/OS/Automation/configure_display.sh` script):

1. Open the terminal on your Raspberry Pi.
2. Follow the [guide](https://askubuntu.com/questions/918707/cant-change-desktop-resolution-size-1920x1080-not-found-in-available-modes)

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
### 3.1 Install the required packages (ensure you're in the virtual environment) and follow this [guide](https://docs.luxonis.com/en/latest/pages/tutorials/first_steps/)

Make sure to run the install_requirements script in the gokark-env:
```bash
python <path-to-install_requirements.py>
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
> If you are not in simulation, you will need to run the can setup script:
```bash
~/OS/Automation/CAN/can-setup.sh
```

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