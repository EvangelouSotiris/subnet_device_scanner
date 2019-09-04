# Network Discovery with Python, using python-nmap library.

## Overview
This network discoverer is a python script that takes a network interface as input and scans the whole subnet with nmap in order to identify other devices, and give information about their hostname/MAC/uptime/ports/services/OS/hardware etc.

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

## Running
- Clone the repository with the two scripts:
```
git clone https://github.com/EvangelouSotiris/python-network-discoverer.git && cd python-network-discoverer
```
- Make sure that you know the interface in which you want to run the network discovery. (You can check the network interfaces using `ip a` , or `ifconfig` in the console).
- Run net_discoverer.py script with sudo:
```
sudo python3 net_discoverer.py <iface>
```

## Author
* **Evangelou Sotiris** - *Developer* - [Github](https://github.com/EvangelouSotiris)
