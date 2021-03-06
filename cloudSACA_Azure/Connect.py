import socket,base64,time,sys,subprocess

EOM="\n\n###"
port=5000
domain=""
def Send (message,retry=True):
	#print message
	global domain,port
	if (isAlive(domain,port,retry)):
		client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		client.connect((domain,port))
		print 'Connected to :' + domain
		print "Port Number :"+str(port)
		client.send(message+EOM)
		chunks=[]
		
		i=0
		while (1):
			buf=client.recv(2048)
			chunks.append(str(buf))
			if (EOM in chunks[-1]):
				res="".join(chunks)[:-5]
				break
		return res
	else:
		print "Server can't be found may be terminated"
		raise Exception("Server can't be found may be terminated")
			

def isAlive(domain,port,retry=True):
	client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	secondTime=False
	result=False
	while (1):
		try:
			client.connect((domain,port))
			client.send("TEST: HELLO\n\n###")
			client.close()
			if secondTime:
				print "Connected To:", domain
			return True
			
		except IOError:
			import time
			time.sleep(5)
			secondTime=True
			print "Trying again...."
		if not retry: break
	return result

#result = isAlive('192.168.167.130',5000)
#print result
