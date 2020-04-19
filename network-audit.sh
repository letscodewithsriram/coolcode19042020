#!/bin/bash

STARTTIME=`date +%s`

echo "SCRIPT-START-TIME: `date`"

while read input

do

	echo "$input"

	### PING TEST

	PING_OUTPUT=`ping -c 2 $input | grep "packet loss" | rev | cut -f5 -d" " | rev`
	echo "$PING_OUTPUT"

	if [ $PING_OUTPUT = "0%" ]; then
		echo "STRING are EQUAL"
	"PING_STATUS=YES"
	else
		echo "STRING are NOT EQUAL"
	fi

	sleep 1

done < input.txt

ENDTIME=`date +%s`

RUNTIME=$(($ENDTIME-$STARTTIME))

echo "TOTAL-AUDIT-RUNTIME = $RUNTIME seconds"

echo "SCRIPT-END-TIME: `date`"
