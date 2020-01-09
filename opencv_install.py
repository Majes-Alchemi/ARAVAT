#!/usr/bin/python3
# File name   : setup.py
# Description : install the software for RPi
# Website     : www.adeept.com
# E-mail      : support@adeept.com
# Author      : William
# Date        : 2018/10/12

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
# Uninstalling and updating

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

# Installing OpenCV4 on Rpi4
# Install Dev tools
for x in range(1,4):
	if os.system("sudo apt-get install build-essential cmake pkg-config") == 0:
		break

# Image I/O packages
for x in range(1,4):
	if os.system("sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng-dev") == 0:
		break

# Video I/O packages
for x in range(1,4):
	if os.system("sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev") == 0:
		break

# GTK development library and prerequisites
# For highgui display
for x in range(1,4):
	if os.system("sudo apt-get install libfontconfig1-dev libcairo2-dev install libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev") == 0:   ####
		break

# OpenCV Optimization
for x in range(1,4):
	if os.system("sudo apt-get install libatlas-base-dev gfortran") == 0:   ####
		break

# HDF5 datasets and Qt GUIs:
for x in range(1,4):
	if os.system("sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5") == 0:   ####
		break

# Python3 Header Files
for x in range(1,4):
	if os.system("sudo apt-get install python3-dev") == 0:
		break

# Install PiCamera API
for x in range(1,4):
	if os.system("pip install "sudo apt-get install python3-picamera") == 0:
		break
for x in range(1,4):
	if os.system("pip install "picamera[array]") == 0:
		break

# Install Virtual Environment
##### TBD ####

# Long Install or Short
While True:
    # main program
    while True:
        answer = input('OpenCV4 has the option of installing through pip or source. The pip installation is recommended for most users. The full installation can take 2-4 hours to install and is recommended for educational and research purposes. Would you like to install the pip version (recommended)?  (y/n): ')
        if answer in ('y', 'n'):
            break
            print('Invalid input.')
            if answer == 'y':
                os.system("pip install opencv-contrib-python==4.1.0.25")
                break
            if answer == 'n':
                print('WARNING!!! Installing OpenCV4 from source.)
                continue

# Are you sure?
While True:
    # main program
    while True:
        answer = input('Installing Open CV4 from source. The full installation can take 2-4 hours and is recommended for educational and research purposes. Would you like to continue? Select (n)o to install the pip version instead. (y/n): ')
        if answer in ('y', 'n'):
            break
            print('Invalid input.')
            if answer == 'n':
                print("Installing Open CV4 with pip.")
                os.system("cpip install opencv-contrib-python==4.1.0.25")
                break
            if answer == 'y':
# Full Install of Open CV4
'''
for x in range(1,4):
	if os.system("cd ~") == 0:   ####
		break

for x in range(1,4):
	if os.system("wget -O opencv.zip https://github.com/opencv/opencv/archive/4.2.0.zip") == 0:
		break

for x in range(1,4):
	if os.system("wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.2.0.zip") == 0:
		break

for x in range(1,4):
	if os.system("unzip opencv.zip") == 0:
		break

for x in range(1,4):
	if os.system("unzip opencv_contrib.zip") == 0:
		break

try:
	os.system('mv opencv-4.2.0 opencv')
except:
	pass

try:
	os.system('mv opencv_contrib-4.2.0 opencv_contrib')
except:
	pass
'''
try:
	os.system('cd ~/opencv/')
	os.system('mkdir build')
    os.system('cd build')
except:
	pass

try:
	os.system('cmake -D CMAKE_BUILD_TYPE=RELEASE \ -D CMAKE_INSTALL_PREFIX=/usr/local \ -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \ -D ENABLE_NEON=ON \ -D ENABLE_VFPV3=ON \ -D WITH_OPENMP=ON \ -D BUILD_TIFF=ON \ -D WITH_FFMPEG=ON \ -D WITH_GSTREAMER=ON \ -D WITH_TBB=ON \ -D BUILD_TBB=ON \ -D BUILD_TESTS=OFF \ -D WITH_EIGEN=OFF \ -D WITH_V4L=ON \ -D WITH_LIBV4L=ON \ -D WITH_VTK=OFF \ -D OPENCV_EXTRA_EXE_LINKER_FLAGS=-latomic \ -D OPENCV_ENABLE_NONFREE=ON \ -D INSTALL_C_EXAMPLES=OFF \ -D INSTALL_PYTHON_EXAMPLES=OFF \ -D BUILD_NEW_PYTHON_SUPPORT=ON \ -D BUILD_opencv_python3=TRUE \ -D OPENCV_GENERATE_PKGCONFIG=ON \ -D BUILD_EXAMPLES=OFF ..')
except:
	pass
'''

file = open('/etc/dphys-swapfile.txt')

try:
os.system('sudo chmod 777 //home/pi/startup.sh')

replace_num('/etc/rc.local','fi','fi\n//home/pi/startup.sh start')








os.system("sudo cp -f //home/pi/adeept_rasptank/server/config.txt //home/pi/config.txt")

os.system("sudo cp -f //home/pi/adeept_rasptank/server/config.txt //etc/config.txt")
os.system("sudo cp -f //home/pi/adeept_rasptank/server/config.txt //config.txt")
print('restarting')

os.system("sudo reboot")
