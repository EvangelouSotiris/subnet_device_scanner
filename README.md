# Network Discovery and Subnet Scanning with Python, using python-nmap library.

## Overview
This network scanner is a python script that takes a network interface as input and scans the whole subnet with nmap in order to identify other devices, and view in a nice human-readable way information about their hostname/MAC/uptime/ports/services/OS/hardware etc.

## Prerequisites
- The user needs to have **sudo priviledges**, as the nmap commands running require sudo for OS inspection.
- Install python-nmap library for python with:
```cmd
pip install python-nmap
```
- Install inetfaces library for python with:
```cmd
pip install netifaces
```
**Troubleshooting**
- If you did pip install the libraries but you are met with the error *ModuleNotFoundError* , please try installing the libraries with apt using:
```cmd
sudo apt install python3-nmap
sudo apt install python3-netifaces
```

## Running
- Clone the repository with the two scripts:
```
git clone https://github.com/EvangelouSotiris/subnet_device_scanner.git && cd subnet_device_scanner
```
- Make sure that you know the interface in which you want to run the network discovery. (You can check the network interfaces using `ip a` , or `ifconfig` in the console).
- Run subnet_device_scanner.py script with sudo:
```
sudo python3 subnet_device_scanner.py <iface>
```
## TODO
implement classless addressing functionality.

## Author
* **Evangelou Sotiris** - *Developer* - [Github](https://github.com/EvangelouSotiris)
