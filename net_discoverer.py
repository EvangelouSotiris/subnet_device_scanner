import nmap
import json
import sys
import socket
from netid_finder import net_id_calculator as calc

LightGreen = "\x1b[92m"
LightRed = "\x1b[91m"
Default = "\x1b[39m"
Cyan = "\x1b[96m"
Magenta = "\x1b[95m"
Black = "\x1b[30m"
Blue = "\x1b[94m"
B_Default = "\x1b[49m"
B_White = "\x1b[107m"

net_id = calc()

print('Searching devices in the network: ' +  net_id )
nm = nmap.PortScanner()
nm.scan(hosts=net_id, arguments='-sP')
nm2 = nmap.PortScanner()
for host in nm.all_hosts():
    result = nm2.scan(hosts=host, arguments='-sV -O -v')
    print(Blue)
    [print('-', end="") for i in range(len(host))]
    print('\n'+B_White + Black + host + B_Default + Blue)
    [print('-', end="") for i in range(len(host))]
    print(Default) 
    main = result['scan'][host]
    del result['nmap']
    del main['portused']
    #print(json.dumps(result, indent=4))
    if main['hostnames'][0]['name'] != '':
        print('Hostname= '+ main['hostnames'][0]['name'])
    if "mac" in main['addresses']:
        mac = main['addresses']['mac']
        print('MAC address= ' + mac)
        if len(main['vendor'])!=0:
            print('Vendor= ' + main['vendor'][mac])
    print('State= '+ LightGreen + main['status']['state'] + Default)
    if 'uptime' in main:
        print('Uptime= '+ str(int(main['uptime']['seconds'])/60) + ' minutes')
    print('TCP Services:')
    for port in main['tcp']:
        print('|-'+ Cyan + main['tcp'][port]['name'] + Default, end="")
        if main['tcp'][port]['version'] != '':
            print('(v. ' + main['tcp'][port]['version']+ ')', end ="")
        print(' at port ' + str(port) + ' - ', end="")
        if main['tcp'][port]['state'] == 'open':
            print(LightGreen + main['tcp'][port]['state'] + Default, end ="")
        else:
            print(LightRed + main['tcp'][port]['state'] + Default, end ="")
        if main['tcp'][port]['product'] != "":
            print( ' - Product: ' + main['tcp'][port]['product'])
        else: print()
    print('Operating System= ' + Magenta + main['osmatch'][0]['name'] + Default)
    print('Common Platform Enumeration:')
    for os in range(len(main['osmatch'][0]['osclass'])):
        print('|-' + main['osmatch'][0]['osclass'][os]['type'] + ' - ' + main['osmatch'][0]['osclass'][os]['cpe'][0])
