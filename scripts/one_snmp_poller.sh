#!/bin/bash

# curl -i -XPOST http://localhost:8086/write?db=na --data-binary "lab,kpi='cpu' value=100 1587885054"

# /usr/bin/snmpwalk -v 2c -c public 192.168.0.110 iso.3.6.1.2.1.1.1.0

## New Measurement -> New OIDs

# /home/tools/network-assess/coolcode19042020/input/one_time_oids.txt

STARTTIME=`date +%s`

echo "SCRIPT-START-TIME: `date`"

`grep "YES,YES,YES" /home/tools/network-assess/coolcode19042020/output/m1-audit/audit.txt > ../input/m2-configs.txt`

echo "# DDL" > model.txt

echo "CREATE DATABASE na" >> model.txt

echo "# DML" >> model.txt

echo "# CONTEXT-DATABASE: na" >> model.txt

while read input

do

        IPADDR=`echo "$input" | cut -f1 -d,`
        echo "$input"

	CISCO_VERSION=`/usr/bin/snmpwalk -v 2c -c public $IPADDR iso.3.6.1.2.1.1.1.0 | grep iso`
	echo "$CISCO_VERSION"

	MODEL=`echo $CISCO_VERSION | cut -f2 -d,`
	SOFTWARE=`echo $CISCO_VERSION | cut -f3 -d,`
	RELEASE=`echo $CISCO_VERSION | cut -f4 -d,`

        echo "model,device=$HOSTNAME,type=MODEL value=\"$MODEL\" $DBS_TIME" >> model.txt
        echo "model,device=$HOSTNAME,type=SOFTWARE value=\"$SOFTWARE\" $DBS_TIME" >> model.txt
        echo "model,device=$HOSTNAME,type=RELEASE value=\"$RELEASE\" $DBS_TIME" >> model.txt

done < ../input/m2-configs.txt

influx -import -path=model.txt -precision=s -database=na

ENDTIME=`date +%s`

RUNTIME=$(($ENDTIME-$STARTTIME))

echo "TOTAL-CONFIGS-RUNTIME = $RUNTIME seconds"

echo "SCRIPT-END-TIME: `date`"

