#!/usr/bin/python3
# File name   : coral_setup.py
# Description : Setting Up Coral USB and other tools for Rpi4
# E-mail      : jamesmx89@gmail.com
# Author      : James Cheung (Majes Alchemi)

import os
import time

def replace_num(file,initial,new_num):
    newline=""
    str_num=str(new_num)
    with open(file,"r") as f:
        for line in f.readlines():
            if(line.find(initial) == 0):
                line = (str_num+'\n')
            newline += line
    with open(file,"w") as f:
        f.writelines(newline)

for x in range(1,4):
	if os.system("sudo apt-get update") == 0:
		break

os.system("sudo apt-get purge -y wolfram-engine")
os.system("sudo apt-get purge -y libreoffice*")
os.system("sudo apt-get -y clean")
os.system("sudo apt-get -y autoremove")

for x in range(1,4):
	if os.system("sudo apt-get -y upgrade") == 0:
		break

# Install Coral Debian Package
for x in range(1,4):
    if os.system("echo 'deb https://packages.cloud.google.com/apt coral-edgetpu-stable main' | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list") == 0:
        break

for x in range(1,4):
	if os.system("curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -") == 0:
		break

for x in range(1,4):
	if os.system("sudo apt-get update") == 0:
		break

# Installing Edge TPU runtime
for x in range(1,4):
	if os.system("sudo apt-get install libedgetpu1-std") == 0:
		break

for x in range(1,4):
	if os.system("sudo pip3 install numpy") == 0:
		break

for x in range(1,4):
	if os.system("sudo apt-get install -y libopencv-dev python3-opencv") == 0:
		break

while True:
    # main program
    while True:
        answer = input('Remove Coral USB and reinsert (y/n): ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.')
    if answer == 'y':
        break
    if answer == 'n':
        print('Remove Coral USB and Reinsert.')
        continue
        break

# Installation of TF LITE
for x in range(1,4):
	if os.system("cd") == 0:
		break

for x in range(1,4):
	if os.system("pip3 install tflite_runtime-1.14.0-cp37-cp37m-linux_armv7l.whl") == 0:
		break

while True:
    # main program
    while True:
        answer = input('Would you like to install Coral with maximum operating frequency? WARNING: Power consumption will be increased and cause the USB TPU to become very hot! Proceed only if you are an advanced user! (y/n): ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.')
    if answer == 'y': os.system("sudo apt-get install libedgetpu1-max")
    if answer == 'n':
        print('TF LITE Install Success! Restarting...')
        break

os.system("sudo reboot")
