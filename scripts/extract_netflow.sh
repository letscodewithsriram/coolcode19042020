
while :
do
	cd /home/tools/network-assess/coolcode19042020/scripts

	./clogin -c 'sh run' 192.168.0.106

	./clogin -c 'ping 192.168.0.125' 192.168.0.106

	ping -c 10 192.168.0.106

	sleep 2
done
