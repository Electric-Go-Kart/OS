#!/bin/bash
# script to test VESC CAN packets
# loop to set rpm to 0
while true
do
  cansend can0 00000301#000003E8
  sleep 0.02 # 1ms
done