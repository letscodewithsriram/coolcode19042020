#!/bin/bash

STARTTIME=`date +%s`

echo "SCRIPT-START-TIME: `date`"

`grep "YES,YES,YES" /home/tools/network-assess/coolcode19042020/output/m1-audit/audit.txt > ../input/m2-configs.txt`

while read input

do

	### CLOGIN TEST

	CLOGIN_OUTPUT=`./clogin -x ../input/commands.txt $input > /home/tools/network-assess/coolcode19042020/output/m2-configs/$input.txt`

	echo "$input"

done < ../input/m2-configs.txt

ENDTIME=`date +%s`

RUNTIME=$(($ENDTIME-$STARTTIME))

echo "TOTAL-CONFIGS-RUNTIME = $RUNTIME seconds"

echo "SCRIPT-END-TIME: `date`"
