#!/bin/bash

# curl -i -XPOST http://localhost:8086/write?db=na --data-binary "lab,kpi='cpu' value=100 1587885054"

STARTTIME=`date +%s`

DBS_TIME=$STARTTIME

echo "$DBS_TIME"

echo "SCRIPT-START-TIME: `date`"

`grep "YES,YES,YES" /home/tools/network-assess/coolcode19042020/output/m1-audit/audit.txt > ../input/m2-configs.txt`

echo "# DDL" > datapts.txt

echo "CREATE DATABASE na" >> datapts.txt

echo "# DML" >> datapts.txt

echo "# CONTEXT-DATABASE: na" >> datapts.txt


while read input

do

	IPADDR=`echo "$input" | cut -f1 -d,`
	# HOSTNAME=`echo "$input" | cut -f2 -d, | tr [:lower:] [:upper:]`
	HOSTNAME="LAB2671"

	# CPU 

	CPU=`/usr/bin/snmpwalk -v 2c -c public $IPADDR 1.3.6.1.4.1.9.2.1.58 | cut -f4 -d' '`
	#!# `curl -i -XPOST http://localhost:8086/write?db=na --data-binary "lab,device=$HOSTNAME,kpi=cpu value=$CPU $DBS_TIME"`

	# Memory

	MEM=`/usr/bin/snmpwalk -v 2c -c public $IPADDR 1.3.6.1.4.1.9.9.48.1.1.1.5.1 | cut -f4 -d' '`
	#!# `curl -i -XPOST http://localhost:8086/write?db=na --data-binary "lab,device=$HOSTNAME,kpi=mem value=$MEM $DBS_TIME"`

	# Temperature

	TEMP=`/usr/bin/snmpwalk -v 2c -c public $IPADDR 1.3.6.1.4.1.9.9.13.1.3.1.6 | cut -f4 -d' '`
	#!# `curl -i -XPOST http://localhost:8086/write?db=na --data-binary "lab,device=$HOSTNAME,kpi=temp value=$TEMP $DBS_TIME"`

	# Power
	
	POW=`/usr/bin/snmpwalk -v 2c -c public $IPADDR 1.3.6.1.4.1.9.9.13.1.5.1.3.1 | cut -f4 -d' '`
	#!# `curl -i -XPOST http://localhost:8086/write?db=na --data-binary "lab,device=$HOSTNAME,kpi=pow value=$POW $DBS_TIME"`

	echo "lab,device=$HOSTNAME,kpi=cpu value=$CPU $DBS_TIME" >> datapts.txt
	echo "lab,device=$HOSTNAME,kpi=mem value=$MEM $DBS_TIME" >> datapts.txt
	echo "lab,device=$HOSTNAME,kpi=temp value=$TEMP $DBS_TIME" >> datapts.txt
	echo "lab,device=$HOSTNAME,kpi=pow value=$POW $DBS_TIME" >> datapts.txt
	
done < ../input/m2-configs.txt

influx -import -path=datapts.txt -precision=s -database=na

ENDTIME=`date +%s`

RUNTIME=$(($ENDTIME-$STARTTIME))

echo "TOTAL-RECURSIVE-POLLER-RUNTIME = $RUNTIME seconds"

echo "SCRIPT-END-TIME: `date`"
