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

	### CLOGIN TEST

	CLOGIN_OUTPUT=`./clogin -c "" $input`
	echo "CLOGIN_OUTPUT"

	sleep 1

done < input.txt

ENDTIME=`date +%s`

RUNTIME=$(($ENDTIME-$STARTTIME))

echo "TOTAL-AUDIT-RUNTIME = $RUNTIME seconds"

echo "SCRIPT-END-TIME: `date`"
