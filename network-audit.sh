#!/bin/bash

STARTTIME=`date +%s`

echo "SCRIPT-START-TIME: `date`"

while read input

do

	#!# echo "$input"

	### PING TEST

	PING_OUTPUT=`ping -c 2 $input | grep "packet loss" | rev | cut -f5 -d" " | rev`
	#!# echo "$PING_OUTPUT"

	if [ $PING_OUTPUT = "0%" ]; then
		PING_STATUS="YES"
	else
		PING_STATUS="NO"
	fi

	echo "$input,$PING_STATUS"

	### SNMP TEST
	
	HOSTNAME=`/usr/bin/snmpwalk -v 2c -c public $input iso.3.6.1.2.1.1.5.0`
	echo "$HOSTNAME"

	CPU_UTILS=`/usr/bin/snmpwalk -v 2c -c public $input 1.3.6.1.4.1.9.2.1.58`
	echo "CPU_UTILS"

	if [[ -n $HOSTNAME ]] && [[ -n $CPU_UTILS ]]; then
		SNMP_STATUS="YES"
	else
		SNMP_STATUS="NO"
	fi

	echo "$input,$PING_STATUS,$SNMP_STATUS"

	### CLOGIN TEST

	CLOGIN_OUTPUT=`./clogin -c "" $input`
	echo "$CLOGIN_OUTPUT"

	sleep 1

done < input.txt

ENDTIME=`date +%s`

RUNTIME=$(($ENDTIME-$STARTTIME))

echo "TOTAL-AUDIT-RUNTIME = $RUNTIME seconds"

echo "SCRIPT-END-TIME: `date`"
