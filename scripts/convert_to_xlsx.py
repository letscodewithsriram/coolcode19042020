#!/usr/bin/python3

import xlsxwriter

dir = "/home/tools/network-assess/coolcode19042020/output/"

workbook = xlsxwriter.Workbook(dir + 'Network-Audit.xlsx')
worksheet = workbook.add_worksheet()

fh = open(dir + "01_network-audit.txt")

row = 4 

# Format

bold = workbook.add_format({'bold': True})

worksheet.write('A2', "TCL NETWORK ASSESSMENT - WAN NETWORK DEVICE ACCESS EXAMINATION MODULE", bold)

worksheet.write('A4', 'LOOPBACK-IP', bold)
worksheet.write('B4', 'HOSTNAME', bold)
worksheet.write('C4', 'ICMP', bold)
worksheet.write('D4', 'SNMP', bold)
worksheet.write('E4', 'SSH', bold)
worksheet.write('F4', 'CPU-UTILS', bold)


for line in fh.readlines():
	line = line.strip()
	datapts = line.split(",")
	# print (datapts) # datapts = ['192.168.0.105', 'gimec-lab-1', 'YES', 'YES', 'YES', '3']
	col = 0
	for data in datapts:
		# print (data) # data = 192.168.0.105
		worksheet.write(row, col, data)
		col = col + 1
	row = row + 1

fh.close()

workbook.close()
