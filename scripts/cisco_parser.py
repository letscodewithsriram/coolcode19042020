from ciscoconfparse import CiscoConfParse

parse = CiscoConfParse("/home/tools/network-assess/coolcode19042020/input/configs/Primary_Hub.txt")

# Interface Section - Column 1

for interface_objs in parse.find_objects("^interface "):
	if interface_objs.re_search_children(" ip address [0-9]"):
		print (interface_objs.text)

for interface_objs in parse.find_objects("^interface "):
	if not interface_objs.re_search_children(" ip address [0-9]"):
		print (interface_objs.text)

# for obj in parse.find_objects("^interface "):
#	print ("Object:", obj.text)
#	print ("Children:", obj.children)
#	for i in obj.children:
#		print (i.text)
#	exit()
