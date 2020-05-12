#!/usr/bin/python3

import xlsxwriter

dir = "/home/tools/network-assess/coolcode19042020/output/"

workbook = xlsxwriter.Workbook(dir + 'reports/03-parsed-network-configs.xlsx')
worksheet = workbook.add_worksheet('Summary')

fh = open(dir + "../input/m2-configs.txt")

row = 4 

# Format

page_header_format = workbook.add_format({
    'bold': 1,
    # 'border': 2,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': '#1e2175',
    'font_name': 'Courier New',
    'font_size': 20,
    'font_color': 'white'
})

column_header_format = workbook.add_format({
    'bold': 1,
    # 'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'font_name': 'Courier New',
    'fg_color': '#521c70',
    'font_size': 12,
    'font_color': 'white'
})

data_format = workbook.add_format({
    'bold': 2,
    'align': 'center',
    'font_name': 'Courier New',
    'valign': 'vcenter',
    'font_size': 10
})

configs_data_format = workbook.add_format({
    'bold': 2,
    # 'align': 'center',
    'font_name': 'Courier New',
    'valign': 'vcenter',
    'font_size': 10
})

summary_icon_format = workbook.add_format({
    'bold': 1,
    'align': 'center',
    'font_name': 'Courier New',
    'valign': 'vcenter',
    'font_size': 8,
    'fg_color': '#008000'
})


worksheet.set_tab_color('gray')
worksheet.set_column('A:A', 10)
worksheet.set_column('B:C', 75)
worksheet.set_row(0, 8)

worksheet.autofilter('A4:C4')
worksheet.freeze_panes(4, 0)

worksheet.merge_range('A2:C2', "TCL NETWORK ASSESSMENT - [M3] WAN NETWORK DEVICE CONFIGURATION PARSER MODULE", page_header_format)

worksheet.write('A4', 'S.No', column_header_format)
worksheet.write('B4', 'LOOPBACK-IP', column_header_format)
worksheet.write('C4', 'HOSTNAME', column_header_format)
#worksheet.write('D4', 'ICMP', column_header_format)
#worksheet.write('E4', 'SNMP', column_header_format)
#worksheet.write('F4', 'SSH', column_header_format)
#worksheet.write('G4', 'CPU-UTILS', column_header_format)

sno = 0

for line in fh.readlines():
	line = line.strip()
	sno = sno + 1
	col = 0
	worksheet.write(row, col, sno, data_format)
	datapts = line.split(",")
	#!# print (datapts[0])# datapts = ['192.168.0.105', 'gimec-lab-1', 'YES', 'YES', 'YES', '3']
	for data in datapts:
		# print (data) # data = 192.168.0.105
		col = col + 1
		worksheet.write_url(row, col,"internal:'" + str(datapts[0]) + "'!A3", string=data, cell_format=data_format)
	row = row + 1

	sheet_name = datapts[0]
	router_sheet = workbook.add_worksheet(sheet_name)
	router_sheet.set_tab_color('green')


	router_sheet.set_column('J:J', 20)
	router_sheet.write_url('B2', "internal:'Summary'!B" + str(sno + 4), string="SUMMARY", cell_format=summary_icon_format)
	router_sheet.merge_range('A3:C3', "PARSED DEVICE CONFIGURATION - " + datapts[0] + "/" + datapts[1], page_header_format)
	router_sheet.merge_range('D3:G3', "", page_header_format)

	# rcfh = open (dir + "m2-configs/" + sheet_name + ".txt", 'r')
	
	from ciscoconfparse import CiscoConfParse

	# parse = CiscoConfParse("/home/tools/network-assess/coolcode19042020/input/configs/Primary_Hub.txt")
	parse = CiscoConfParse("/network-assess/coolcode19042020/input/configs/Primary_Hub.txt")

	# Interface Section - Column 1

	rs_col = 0

	rs_row = 6

	router_sheet.write('A5', 'Interface Context', column_header_format)
	
	router_sheet.set_column('A:A', 75)

	router_sheet.write(rs_row, rs_col, 'Interfaces - With IP Address', column_header_format)

	rs_row = rs_row + 2

	for interface_objs in parse.find_objects("^interface "):
		if interface_objs.re_search_children(" ip address [0-9]"):
			config_line = interface_objs.text.strip()
			router_sheet.write(rs_row, rs_col, config_line, configs_data_format)
			rs_row = rs_row + 1

			for interface_line in interface_objs.children:
				interface_line = interface_line.text.strip()
				router_sheet.write(rs_row, rs_col, interface_line, configs_data_format)
				rs_row = rs_row + 1

			rs_row = rs_row + 1

	rs_row = rs_row + 2

	router_sheet.write(rs_row, rs_col, 'Interfaces - Without IP Address', column_header_format)

	rs_row = rs_row + 2

	for interface_objs in parse.find_objects("^interface "):
		if not interface_objs.re_search_children(" ip address [0-9]"):
			config_line = interface_objs.text.strip()
			router_sheet.write(rs_row, rs_col, config_line, configs_data_format)
			rs_row = rs_row + 1

			for interface_line in interface_objs.children:
				interface_line = interface_line.text.strip()
				router_sheet.write(rs_row, rs_col, interface_line, configs_data_format)
				rs_row = rs_row + 1

			rs_row = rs_row + 1

	# Routing Context - Column 2

	rs_col = 1

	rs_row = 6

	router_sheet.write('B5', 'Routing Context', column_header_format)

	router_sheet.set_column('B:B', 75)

	router_sheet.write(rs_row, rs_col, 'OSPF', column_header_format)

	rs_row = rs_row + 2

	for routing_objs in parse.find_objects("^router ospf "):
		config_line = routing_objs.text.strip()
		router_sheet.write(rs_row, rs_col, config_line, configs_data_format)
		rs_row = rs_row + 1

		for routing_line in routing_objs.children:
			routing_line = routing_line.text.strip()
			router_sheet.write(rs_row, rs_col, routing_line, configs_data_format)
			rs_row = rs_row + 1

	rs_row = rs_row + 2

	router_sheet.write(rs_row, rs_col, 'BGP', column_header_format)

	rs_row = rs_row + 2

	for routing_objs in parse.find_objects("^router bgp "):
		config_line = routing_objs.text.strip()
		router_sheet.write(rs_row, rs_col, config_line, configs_data_format)
		rs_row = rs_row + 1

		for routing_line in routing_objs.children:
			routing_line = routing_line.text.strip()
			router_sheet.write(rs_row, rs_col, routing_line, configs_data_format)
			rs_row = rs_row + 1

	rs_row = rs_row + 2

	router_sheet.write(rs_row, rs_col, 'EIGRP', column_header_format)

	rs_row = rs_row + 2

	for routing_objs in parse.find_objects("^router eigrp "):
		config_line = routing_objs.text.strip()
		router_sheet.write(rs_row, rs_col, config_line, configs_data_format)
		rs_row = rs_row + 1

		for routing_line in routing_objs.children:
			routing_line = routing_line.text.strip()
			router_sheet.write(rs_row, rs_col, routing_line, configs_data_format)
			rs_row = rs_row + 1

		rs_row = rs_row + 1

	rs_row = rs_row + 2

	router_sheet.write(rs_row, rs_col, 'RIP', column_header_format)

	rs_row = rs_row + 2

	for routing_objs in parse.find_objects("^router rip "):
		config_line = routing_objs.text.strip()
		router_sheet.write(rs_row, rs_col, config_line, configs_data_format)
		rs_row = rs_row + 1

		for routing_line in routing_objs.children:
			routing_line = routing_line.text.strip()
			router_sheet.write(rs_row, rs_col, routing_line, configs_data_format)
			rs_row = rs_row + 1

		rs_row = rs_row + 1

	rs_row = rs_row + 2

	router_sheet.write(rs_row, rs_col, 'STATIC', column_header_format)

	rs_row = rs_row + 2

	for routing_objs in parse.find_objects("^ip route "):
		config_line = routing_objs.text.strip()
		router_sheet.write(rs_row, rs_col, config_line, configs_data_format)
		rs_row = rs_row + 1

		for routing_line in routing_objs.children:
			routing_line = routing_line.text.strip()
			router_sheet.write(rs_row, rs_col, routing_line, configs_data_format)
			rs_row = rs_row + 1

	rs_row = rs_row + 2

	# Route Filters & Manipulations - Column 3

	rs_col = 2
	
	rs_row = 6

	router_sheet.write('C5', "Router Filters & Manipulations", column_header_format)

	router_sheet.set_column('C:C', 75)

	router_sheet.write(rs_row, rs_col, 'Route-Map', column_header_format)

	rs_row = rs_row + 2

	for routing_objs in parse.find_objects("^route-map "):
		config_line = routing_objs.text.strip()
		router_sheet.write(rs_row, rs_col, config_line, configs_data_format)
		rs_row = rs_row + 1

		for routing_line in routing_objs.children:
			routing_line = routing_line.text.strip()
			router_sheet.write(rs_row, rs_col, routing_line, configs_data_format)
			rs_row = rs_row + 1
		rs_row = rs_row + 1

	rs_row = rs_row + 2
	
	router_sheet.write(rs_row, rs_col, 'Prefix-List', column_header_format)
	
	rs_row = rs_row + 2

	for routing_objs in parse.find_objects("^ip prefix-list "):
		config_line = routing_objs.text.strip()
		router_sheet.write(rs_row, rs_col, config_line, configs_data_format)
		rs_row = rs_row + 1

		for routing_line in routing_objs.children:
			routing_line = routing_line.text.strip()
			router_sheet.write(rs_row, rs_col, routing_line, configs_data_format)
			rs_row = rs_row + 1

		rs_row = rs_row + 1

	rs_row = rs_row + 2

	router_sheet.write(rs_row, rs_col, 'Access-List', column_header_format)

	rs_row = rs_row + 2

	for routing_objs in parse.find_objects("access-list "):
		config_line = routing_objs.text.strip()
		router_sheet.write(rs_row, rs_col, config_line, configs_data_format)
		rs_row = rs_row + 1

		for routing_line in routing_objs.children:
			routing_line = routing_line.text.strip()
			router_sheet.write(rs_row, rs_col, routing_line, configs_data_format)
			rs_row = rs_row + 1

		rs_row = rs_row + 1

	rs_row = rs_row + 2

	# QoS Context - Column 4

	rs_col = 3

	rs_row = 6

	router_sheet.write('D5', 'QoS Context', column_header_format)

	router_sheet.set_column('D:D', 75)

	router_sheet.write(rs_row, rs_col, 'Class Map', column_header_format)

	rs_row = rs_row + 2

	for routing_objs in parse.find_objects("^class-map "):
		config_line = routing_objs.text.strip()
		router_sheet.write(rs_row, rs_col, config_line, configs_data_format)
		rs_row = rs_row + 1

		for routing_line in routing_objs.children:
			routing_line = routing_line.text.strip()
			router_sheet.write(rs_row, rs_col, routing_line, configs_data_format)
			rs_row = rs_row + 1
		rs_row = rs_row + 1

	rs_row = rs_row + 2

	router_sheet.write(rs_row, rs_col, 'Policy Map', column_header_format)

	rs_row = rs_row + 2

	for routing_objs in parse.find_objects("^policy-map "):
		config_line = routing_objs.text.strip()
		router_sheet.write(rs_row, rs_col, config_line, configs_data_format)
		rs_row = rs_row + 1

		for routing_line in routing_objs.children:
			routing_line = routing_line.text.strip()
			router_sheet.write(rs_row, rs_col, routing_line, configs_data_format)
			rs_row = rs_row + 1

		rs_row = rs_row + 1

	rs_row = rs_row + 2

	# Service Management - Column 5

	rs_col = 4

	rs_row = 6

	router_sheet.write('E5', 'Service Management', column_header_format)

	router_sheet.set_column('E:E', 75)

	router_sheet.write(rs_row, rs_col, 'IP-SLA', column_header_format)

	rs_row = rs_row + 2

	for routing_objs in parse.find_objects("^ip sla "):
		config_line = routing_objs.text.strip()
		router_sheet.write(rs_row, rs_col, config_line, configs_data_format)
		rs_row = rs_row + 1

		for routing_line in routing_objs.children:
			routing_line = routing_line.text.strip()
			router_sheet.write(rs_row, rs_col, routing_line, configs_data_format)
			rs_row = rs_row + 1
		rs_row = rs_row + 1

	rs_row = rs_row + 2

	router_sheet.write(rs_row, rs_col, 'Logging', column_header_format)

	rs_row = rs_row + 2

	for routing_objs in parse.find_objects("^logging "):
		config_line = routing_objs.text.strip()
		router_sheet.write(rs_row, rs_col, config_line, configs_data_format)
		rs_row = rs_row + 1

		for routing_line in routing_objs.children:
			routing_line = routing_line.text.strip()
			router_sheet.write(rs_row, rs_col, routing_line, configs_data_format)
			rs_row = rs_row + 1

		rs_row = rs_row + 1

	rs_row = rs_row + 2

	router_sheet.write(rs_row, rs_col, 'SNMP', column_header_format)

	rs_row = rs_row + 2

	for routing_objs in parse.find_objects("^snmp "):
		config_line = routing_objs.text.strip()
		router_sheet.write(rs_row, rs_col, config_line, configs_data_format)
		rs_row = rs_row + 1
		
		for routing_line in routing_objs.children:
			routing_line = routing_line.text.strip()
			router_sheet.write(rs_row, rs_col, routing_line, configs_data_format)
			rs_row = rs_row + 1

		rs_row = rs_row + 1

	rs_row = rs_row + 2

	router_sheet.write(rs_row, rs_col, 'NTP', column_header_format)

	rs_row = rs_row + 2

	for routing_objs in parse.find_objects("^ntp "):
		config_line = routing_objs.text.strip()
		router_sheet.write(rs_row, rs_col, config_line, configs_data_format)
		rs_row = rs_row + 1

		for routing_line in routing_objs.children:
			routing_line = routing_line.text.strip()
			router_sheet.write(rs_row, rs_col, routing_line, configs_data_format)
			rs_row = rs_row + 1

		rs_row = rs_row + 1

	rs_row = rs_row + 2

	# Management Plane - Column 6

	rs_col = 5
	
	rs_row = 6

	router_sheet.write('F5', 'Management Plane', column_header_format)

	router_sheet.set_column('F:F', 75)

	router_sheet.write(rs_row, rs_col, 'Line VTY', column_header_format)

	rs_row = rs_row + 2

	for routing_objs in parse.find_objects("^line vty "):
		config_line = routing_objs.text.strip()
		router_sheet.write(rs_row, rs_col, config_line, configs_data_format)
		rs_row = rs_row + 1

		for routing_line in routing_objs.children:
			routing_line = routing_line.text.strip()
			router_sheet.write(rs_row, rs_col, routing_line, configs_data_format)
			rs_row = rs_row + 1

		rs_row = rs_row + 1

	rs_row = rs_row + 2

	router_sheet.write(rs_row, rs_col, 'Username', column_header_format)

	rs_row = rs_row + 2

	for routing_objs in parse.find_objects("^username "):
		config_line = routing_objs.text.strip()
		router_sheet.write(rs_row, rs_col, config_line, configs_data_format)
		rs_row = rs_row + 1

		for routing_line in routing_objs.children:
			routing_line = routing_line.text.strip()
			router_sheet.write(rs_row, rs_col, routing_line, configs_data_format)
			rs_row = rs_row + 1

		rs_row = rs_row + 1
		
	rs_row = rs_row + 2

	router_sheet.write(rs_row, rs_col, 'AAA Authentication', column_header_format)

	rs_row = rs_row + 2

	for routing_objs in parse.find_objects("^aaa "):
		config_line = routing_objs.text.strip()
		router_sheet.write(rs_row, rs_col, config_line, configs_data_format)
		rs_row = rs_row + 1

		for routing_line in routing_objs.children:
			routing_line = routing_line.text.strip()
			router_sheet.write(rs_row, rs_col, routing_line, configs_data_format)
			rs_row = rs_row + 1

		rs_row = rs_row + 1

	rs_row = rs_row + 2

	# Crypto Context - Column 6

	rs_col = 6

	rs_row = 6

	router_sheet.write('G5', 'Crypto Context', column_header_format)

	router_sheet.set_column('G:G', 75)

	router_sheet.write(rs_row, rs_col, 'Crypto Commands', column_header_format)

	rs_row = rs_row + 2

	for routing_objs in parse.find_objects("^crypto "):
		config_line = routing_objs.text.strip()
		if not "certificate" in config_line:
			router_sheet.write(rs_row, rs_col, config_line, configs_data_format)
			rs_row = rs_row + 1

			for routing_line in routing_objs.children:
				routing_line = routing_line.text.strip()
				router_sheet.write(rs_row, rs_col, routing_line, configs_data_format)
				rs_row = rs_row + 1

			rs_row = rs_row + 1

	rs_row = rs_row + 2

	# Unfiltered Other Configurations - Column 7

	rs_col = 7
	
	rs_row = 6

	router_sheet.write('H5', 'Unfiltered Other Configuration', column_header_format)

	router_sheet.set_column('H:H', 75)

	router_sheet.write(rs_row, rs_col, 'Remaining Configurations', column_header_format)

	rs_row = rs_row + 2

	for routing_objs in parse.find_objects("



fh.close()

workbook.close()
