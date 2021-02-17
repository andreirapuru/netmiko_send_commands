#Author: Andre Ortega, brainwork.com.br, https://github.com/andreirapuru/netmiko_script_automation

import getpass
import netmiko
import csv
import logging
from datetime import datetime
from netmiko import ConnectHandler

#Enable debug (optional)
#logging.basicConfig(filename='netmiko_logs.txt', level=logging.DEBUG)
#logger = logging.getLogger("netmiko")

print('\n''Script initiated')
print('\n')

#Get credentials (same for all devices)
UN = input('Username: ')
PW = getpass.getpass('Password: ')
EN = getpass.getpass('Enable: ')

#Defautl template with credentials
device_template = {
'device_type': 'cisco',
'ip': '1.1.1.1',
'username': UN,
'password': PW,
'port':1111,
'secret': EN,
'blocking_timeout': 4 #Default = 8, if timeout problem increase to 16
}

#Open file with devices informations (IP and Port)
list_of_devices = csv.DictReader(open('devices_to_configure.csv'))

#Prepar device_template with information from CSV
for row in list_of_devices:
	if (row['port']) == '23':
		device_template['device_type'] = 'cisco_ios_telnet'
		device_template['port'] = '23'
	else:
		device_template['device_type'] = 'cisco_ios'
		device_template['port'] = '22'
	device_template['ip'] = row['ip']
	try:
		print ('====== Login device ', device_template['ip'],' ======')
		#Connect to device and send config
		net_connect = ConnectHandler(**device_template)
		net_connect.enable()
		output = net_connect.send_config_from_file('commands_to_send.txt')
		print(output)
		#Save logs in file
		log = open('log_file.txt', 'a')
		log.write('\n')
		log.write(device_template['ip'])
		log.write('\n')
		log.write(output)
		log.write('\n')
		net_connect.disconnect()
		print ('====== Logout device', device_template['ip'],' ======')
	except:
		log = open('log_file.txt', 'a')
		log.write('\n')
		log.write('Couldnt access the device ')
		log.write(device_template['ip'])
		log.write('\n')
		print ('Couldnt access device', device_template['ip'],' =====')
log.close()
print('\n' 'Script finished')
