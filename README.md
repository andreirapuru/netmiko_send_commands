# Netmiko Send Commands
Script to send commands from a file to a list of devices (routers and switches running IOS).
The output is saved in a .txt.

# Requires:
- Python (tested on Python 2.7 and 3.6)
- Modules
  - Netmiko >= 2.2.2
  - getpass
  - csv
  - You can use pip install -r requirements.txt to install all modules

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
![devices](https://user-images.githubusercontent.com/17407109/108557485-71efad00-72d7-11eb-8ca6-33b452f9e621.PNG)
3) Put the configuration that you want to send to devices in file commands_to_send.txt (it starts in config mode)
![commands](https://user-images.githubusercontent.com/17407109/108557453-64d2be00-72d7-11eb-8c7f-e00e3676a834.PNG)
4) Run config_devices_from_file.py
![send~](https://user-images.githubusercontent.com/17407109/108557282-1c1b0500-72d7-11eb-8b25-2134fa2e6403.PNG)
5) Inform username, password and enable

# Use case:
- to perform backup, to enables logging, to collects information, to creates username, shut/no shut interfaces, to removes config, any other config/command that can be repeated over different devices

# Getting Help
If you are having trouble or need help, create an issue [here](https://github.com/andreirapuru/netmiko_send_commands/issues)

# Credits and references
- All credits to Kirk Byers for making [Netmiko](https://github.com/ktbyers/netmiko)


[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/andreirapuru/netmiko_send_commands)
