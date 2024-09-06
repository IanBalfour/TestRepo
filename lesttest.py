import subprocess
import time
import socket

c = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while(True):
	for i in range(0,576):
		h = (i << 6) + c
		one = chr(h >> 8)
		two = chr(h & 255)
		h = one + two
		print(h)
		sock.sendto(h.encode('utf-8'),('192.168.1.69', 4210))
		time.sleep(3)
	
	
		'''
		h = str(hex((i << 6) + c))
		h = h[2:]
		while(len(h) < 4):
			h = '0' + h
		j = '\\x' + h[0:2] + '\\x' + h[2:]
		l = "echo -e \'" + j + "\' | nc -u 192.168.1.69 4210 -q 0"
		print(l)
		#subprocess.call(l, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		sock.sendto(j.encode('utf-8'), ('192.168.1.69',4210))
		time.sleep(5)'''
		
	c = (c + 1) % 3
