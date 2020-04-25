#!/usr/bin/python3

import xlsxwriter

dir = "/home/tools/network-assess/coolcode19042020/output/"

workbook = xlsxwriter.Workbook(dir + 'reports/01-Network-Audit.xlsx')
worksheet = workbook.add_worksheet('NE-AUDIT')

fh = open(dir + "m1-audit/audit.txt")

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

worksheet.set_tab_color('gray')
worksheet.set_column('A:A', 10)
worksheet.set_column('B:G', 30)
worksheet.set_row(0, 8)

worksheet.autofilter('A4:G4')
worksheet.freeze_panes(4, 0)

worksheet.merge_range('A2:G2', "TCL NETWORK ASSESSMENT - WAN NETWORK DEVICE ACCESS EXAMINATION MODULE", page_header_format)

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
	# print (datapts) # datapts = ['192.168.0.105', 'gimec-lab-1', 'YES', 'YES', 'YES', '3']
	for data in datapts:
		# print (data) # data = 192.168.0.105
		col = col + 1
		worksheet.write(row, col, data, data_format)
	row = row + 1

fh.close()

workbook.close()
