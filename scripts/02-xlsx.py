#!/usr/bin/python3

import xlsxwriter

dir = "/home/tools/network-assess/coolcode19042020/output/"

workbook = xlsxwriter.Workbook(dir + 'reports/02-network-configs.xlsx')
worksheet = workbook.add_worksheet()

fh = open(dir + "../input/m2-configs.txt")

row = 4 

# Format

bold = workbook.add_format({'bold': True})

worksheet.write('A2', "TCL NETWORK ASSESSMENT - WAN NETWORK DEVICE CONFIGURATION EXTRACTION MODULE", bold)

worksheet.write('A4', 'LOOPBACK-IP', bold)
worksheet.write('B4', 'HOSTNAME', bold)

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
