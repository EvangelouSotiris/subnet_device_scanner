import nmap
import json
import sys
import socket

DEFAULT_CIDR=24
local_ip = socket.gethostbyname(socket.gethostname())
if DEFAULT_CIDR == 24:
    net_id = local_ip.split('.')[0]+'.'+local_ip.split('.')[1]+'.'+local_ip.split('.')[2]+'.0/24'

print('Searching devices in the network: ' +  net_id)
nm = nmap.PortScanner()
nm.scan(hosts=net_id, arguments='-sP')
nm2 = nmap.PortScanner()
for host in nm.all_hosts():
    [print('-', end="") for i in range(len(host))]
    print('\n'+host)
    [print('-', end="") for i in range(len(host))]
    print()
    result = nm2.scan(hosts=host, arguments='-sV -O -v')
    main = result['scan'][host]
    del result['nmap']
    del main['portused']
    #print(json.dumps(result, indent=4))
    print('Hostname= '+ main['hostnames'][0]['name'])
    if "mac" in main['addresses']:
        mac = main['addresses']['mac']
        print('MAC address= ' + mac)
        if len(main['vendor'])!=0:
            print('Vendor= ' + main['vendor'][mac])
    print('State= ' + main['status']['state'])
    if 'uptime' in main:
        print('Uptime= '+ str(int(main['uptime']['seconds'])/60) + ' minutes')
    print('TCP Services:')
    for port in main['tcp']:
        print('|-' + main['tcp'][port]['name'], end="")
        if main['tcp'][port]['version'] != '':
            print('(v. ' + main['tcp'][port]['version']+ ')', end ="")
        print(' at port ' + str(port) + ' - ' + main['tcp'][port]['state'], end ="")
        if main['tcp'][port]['product'] != "":
            print( ' - Product: ' + main['tcp'][port]['product'])
        else: print()
    print('Operating System= ' + main['osmatch'][0]['name'])
    print('Common Platform Enumeration:')
    for os in range(len(main['osmatch'][0]['osclass'])):
        print('|-' + main['osmatch'][0]['osclass'][os]['type'] + ' - ' + main['osmatch'][0]['osclass'][os]['cpe'][0])
