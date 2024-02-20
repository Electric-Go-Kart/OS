import can
import time
from enum import IntEnum
import struct
################## CSU Electric Racing Kart CAN Interface Tool ##################
# https://github.com/Electric-Go-Kart/VESC/blob/main/comm_can.md                #
#                                                                               #
# This script is a simple command-line interface for emulating a VESC motor     #
# controller. It allows the user to send status messages and receive commands.  #
#                                                                               #
# Note: When sending commands outside of range they will be truncated at the    #
# range limit. For example, if the maximum braking current is set to 50A and    #
# CAN_PACKET_SET_CURRENT_BRAKE is sent with 60A the value will be truncated and #
# 50A will be used.                                                             #
#################################################################################

# VESC ID and CAN interface
VESC_ID = int(input("Enter your VESC ID: "))
CAN_INTERFACE = input("Enter your vcan interface (e.g. vcan0): ")

# Message types and IDs
class MessageType(IntEnum):
    CAN_PACKET_SET_DUTY = 0,
    CAN_PACKET_SET_CURRENT = 1,
    CAN_PACKET_SET_CURRENT_BRAKE = 2,
    CAN_PACKET_SET_RPM = 3,
    CAN_PACKET_SET_POS = 4,
    CAN_PACKET_SET_CURRENT_REL = 10,
    CAN_PACKET_SET_CURRENT_BRAKE_REL = 11,
    CAN_PACKET_SET_CURRENT_HANDBRAKE = 12,
    CAN_PACKET_SET_CURRENT_HANDBRAKE_REL = 13,
    CAN_PACKET_STATUS = 9,
    CAN_PACKET_STATUS_2 = 14,
    CAN_PACKET_STATUS_3 = 15,
    CAN_PACKET_STATUS_4 = 16,
    CAN_PACKET_STATUS_5 = 27,
    CAN_PACKET_STATUS_6 = 28

###### Message sending and receiving function ######
def create_message(command_id, data):
    # Create a CAN message with the VESC ID and the command ID
    can_id = (command_id << 8) | VESC_ID
    # Convert the data to a 4-byte big endian signed integer
    data_bytes = struct.pack('>i', data)
    message = can.Message(arbitration_id=can_id, data=data_bytes, is_extended_id=True)
    return message

def send_message(bus, message, num_repeat):
    for i in range(num_repeat):
        bus.send(message)

# Create CAN bus object
bus = can.interface.Bus(channel=CAN_INTERFACE, bustype='socketcan')

num_repeat = int(input("Enter the number of times to repeat the message: "))

# Main loop
while True:
    command_name = input("Enter the command name (see https://github.com/Electric-Go-Kart/VESC/blob/main/comm_can.md for details): ")
    command_id = MessageType[command_name]
    print("Command ID: ", command_id)
    if command_id == MessageType.CAN_PACKET_SET_DUTY:
        duty = float(input("Enter the duty cycle (between -1 and 1): "))
        message = create_message(command_id, int(duty * 100000)) # Unit: % / 100
        send_message(bus, message, num_repeat)
    elif command_id == MessageType.CAN_PACKET_SET_CURRENT:
        current = float(input("Enter the current (A) (between -MOTOR_MAX and MOTOR_MAX): "))
        message = create_message(command_id, int(current * 1000)) # Unit: A
        send_message(bus, message, num_repeat)
    elif command_id == MessageType.CAN_PACKET_SET_CURRENT_BRAKE:
        current = float(input("Enter the current (A) (between -MOTOR_MAX and MOTOR_MAX): "))
        message = create_message(command_id, int(current * 1000)) # Unit: A
        send_message(bus, message, num_repeat)
    elif command_id == MessageType.CAN_PACKET_SET_RPM:
        rpm = int(input("Enter the RPM (between -MAX_RPM and MAX_RPM): "))
        message = create_message(command_id, rpm) # Unit: RPM
        bus.send(message)
    elif command_id == MessageType.CAN_PACKET_SET_POS:
        pos = float(input("Enter the position (between 0 and 360): "))
        message = create_message(command_id, int(pos * 1000000)) # Unit: Degrees
        send_message(bus, message, num_repeat)
    elif command_id == MessageType.CAN_PACKET_SET_CURRENT_REL:
        current = float(input("Enter the current (A) (between -1 and 1): "))
        message = create_message(command_id, int(current * 100000)) # Unit: % / 100
        send_message(bus, message, num_repeat)
    elif command_id == MessageType.CAN_PACKET_SET_CURRENT_BRAKE_REL:
        current = float(input("Enter the current (A) (between -1 and 1): "))
        message = create_message(command_id, int(current * 100000)) # Unit: % / 100
        send_message(bus, message, num_repeat)
    elif command_id == MessageType.CAN_PACKET_SET_CURRENT_HANDBRAKE:
        current = float(input("Enter the current (A) (between -MOTOR_MAX and MOTOR_MAX): "))
        message = create_message(command_id, int(current * 1000)) # Unit: A
        send_message(bus, message, num_repeat)
    elif command_id == MessageType.CAN_PACKET_SET_CURRENT_HANDBRAKE_REL:
        current = float(input("Enter the current (A) (between -1 and 1): "))
        message = create_message(command_id, int(current * 100000)) # Unit: % / 100
        send_message(bus, message, num_repeat)
    else:
        print("Invalid command name")
        continue

    # Wait for a status message
    if CAN_INTERFACE[0:4] == "vcan":
        time.sleep(0.1)
    else:
        message = bus.recv(1)
        if message is not None:
            print("Received message: ", message)
        else:
            print("No message received")
        