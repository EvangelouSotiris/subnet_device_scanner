import socket
import fcntl
import struct
import sys
import netifaces

def net_id_calculator(iface):
    
    if iface not in netifaces.interfaces():
        print("There is no network interface named " + iface + ".")
        sys.exit(1)
    classfull_addressing=[0,8,16,24,32]
    if netifaces.AF_INET not in netifaces.ifaddresses(iface):
        print("No IP corresponding to that interface.")
        exit(1)
    netmask = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['netmask']
    local_ip = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']
   
    ip_parts = local_ip.split('.')
    pieces = netmask.split('.')
    netmask_parts = ['','','','']
    total_1s = 0
    for i in range(len(pieces)):
        netmask_parts[i] = str("{0:08b}".format(int(pieces[i])))
        for bit in netmask_parts[i]:
            if bit == '1':
                total_1s += 1
                continue
    CIDR = total_1s

    if CIDR in classfull_addressing:
        if CIDR == 0:
            return '0.0.0.0/'+str(CIDR)
        elif CIDR == 8:
            return ip_parts[0]+'.0.0.0/'+str(CIDR)
        elif CIDR == 16:
            return ip_parts[0]+'.'+ip_parts[1]+'.0.0/'+str(CIDR)
        elif CIDR == 24:
            return ip_parts[0]+'.'+ip_parts[1]+'.'+ip_parts[2]+'.0/'+str(CIDR)
        else:
            print('No hosts available in a network with CIDR notation 32. Exiting')
            sys.exit(0)
