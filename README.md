# Netmiko Send Commands
Script to send configuration from a file to a list of devices (routers and switches running IOS).

# Requires:
- Python (tested on Python 2.7 and 3.6)
- Netmiko >= 2.2.2
- import getpass
- import csv
- import logging
- datetime

# Supports:
- Routers and Switches Cisco running IOS with SSH/Telnet configured (default ports 22/23)

# Limitations:
- Same credentials for all devices
- Only SSH/Telnet with default ports (22/23)
- Last line on configuration file can not be 'exit'
- Only config that can be the same in different devices

# Usage:
1) Download this repository or copy all of the content config_devices_from_file.py file into a python file
2) Inform port (22/23) and IP address of devices in devices_to_configure.csv file
3) Put the configuration that you want to send to devices in file commands_to_send.txt (it starts in config mode)
4) Run config_devices_from_file.py
5) Inform username, password and enable

![Output](https://raw.githubusercontent.com/andreirapuru/netmiko_send_commands/main/send_commands.PNG)

# Use case:
- to perform backup, to enables logging, to collects information, to creates username, shut/no shut interfaces, to removes config, any other config/command that can be repeated over different devices

# Getting Help
If you are having trouble or need help, create an issue [here](https://github.com/andreirapuru/netmiko_send_commands/issues)

# Credits and references
- All credits to Kirk Byers for making [Netmiko](https://github.com/ktbyers/netmiko)
