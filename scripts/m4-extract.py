import sys

import re

import os

from ciscoconfparse import CiscoConfParse

routers = os.listdir("/home/tools/network-assess/coolcode19042020/input/configs")

search_type = sys.argv[1].strip()

user_patterns = sys.argv[2].split(';')

# Interface Section

#!# python3 m4-extract.py "interface" "no ip proxy;speed"

def interface_configs(user_patterns):
	for interface_objs in parse.find_objects("^interface "):
		if interface_objs.re_search_children(" ip address [0-9]"):
			config_line = interface_objs.text.strip()
			# print (config_line)
			cmd_flag = 0

			for interface_line in interface_objs.children:
				interface_line = interface_line.text.strip()
				for cmd in user_patterns:
					cmd = str(cmd.strip())
					if re.search(cmd, interface_line):
						cmd_flag = cmd_flag + 1
						#!# print (router_name + "," +  config_line + "," + interface_line)

			if cmd_flag == len(user_patterns):
				print (router_name + "," +  config_line.split(" ")[1] + ",YES")
			elif cmd_flag == 0:
				print (router_name + "," +  config_line.split(" ")[1] + ",NO")
			else:
				print (router_name + "," +  config_line.split(" ")[1] + ",PARTIAL")

# Global Section 

def global_configs(user_patterns):
	cmd_flag = 0
	for global_objs in parse.find_objects("^[a-z]"):
		config_line = global_objs.text.strip()
		if "interface " not in config_line:
			for cmd in user_patterns:
				cmd = str(cmd)
				if re.search(cmd, config_line):
					cmd_flag = cmd_flag + 1
					print (router_name + "," +  config_line)

#!# eval(search_type)(user_patterns)

for router_name in routers:

	#!# router_name="ad2-t1-cr04"

	parse = CiscoConfParse("/home/tools/network-assess/coolcode19042020/input/configs/" + router_name)

	eval(search_type)(user_patterns)
