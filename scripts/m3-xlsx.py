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
worksheet.set_column('B:G', 30)
worksheet.set_row(0, 8)

worksheet.autofilter('A4:G4')
worksheet.freeze_panes(4, 0)

worksheet.merge_range('A2:G2', "TCL NETWORK ASSESSMENT - [M3] WAN NETWORK DEVICE CONFIGURATION PARSER MODULE", page_header_format)

worksheet.write('A4', 'S.No', column_header_format)
worksheet.write('B4', 'LOOPBACK-IP', column_header_format)
worksheet.write('C4', 'HOSTNAME', column_header_format)
worksheet.write('D4', 'ICMP', column_header_format)
worksheet.write('E4', 'SNMP', column_header_format)
worksheet.write('F4', 'SSH', column_header_format)
worksheet.write('G4', 'CPU-UTILS', column_header_format)

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
	router_sheet.write_url('J2', "internal:'Summary'!B" + str(sno + 4), string="SUMMARY", cell_format=summary_icon_format)
	router_sheet.merge_range('A3:U3', "PARSED DEVICE CONFIGURATION - " + datapts[0] + "/" + datapts[1], page_header_format)

	rs_row = 6

	# rcfh = open (dir + "m2-configs/" + sheet_name + ".txt", 'r')
	
	from ciscoconfparse import CiscoConfParse

	parse = CiscoConfParse("/home/tools/network-assess/coolcode19042020/input/configs/Primary_Hub.txt")

	# Interface Section - Column 1

	rs_col = 0

	router_sheet.write('A5', 'Interface Context - With IP Address', column_header_format)
	
	router_sheet.set_column('A:A', 75)

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

	router_sheet.write(rs_row, rs_col, 'Interface Context - Without IP Address', column_header_format)

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

	router_sheet.write('B5', 'Routing Context', column_header_format)

	router_sheet.set_column('B:B', 75)

	rs_row = 4 
	
	router_sheet.write(rs_row, rs_col, 'OSPF', column_header_format)

	rs_row = rs_row + 2

	for routing_objs in parse.find_object("^router ospf "):
		for routing_line in routing_objs.children:
			routing_line = routing_line.strip()
			router_sheet.write(rs_row, rs_col, routing_line, configs_data_format)`	
			rs_row = rs_row + 1


	rs_row = rs_row + 2

	router_sheet.write(rs_row, rs_col, 'BGP', column_header_format)

	rs_row = rs_row + 2

	for routing_objs in parse.find_object("^router bgp "):
		for routing_line in routing_objs.children:
			routing_line = routing_line.strip()
			router_sheet.write(rs_row, rs_col, routing_line, configs_data_format
			rs_row = rs_row + 1

	rs_row = rs_row + 2
	
fh.close()

workbook.close()
