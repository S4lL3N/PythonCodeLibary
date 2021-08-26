# docs.micropython.org/en/latest/esp32/quickref.html

#to call using the repl import file name (internet)
#EXAMPLE= import internet
#then type the file name and the function
#EXAMPLE= internet.connect()

ip = None

def connect():
	import network
	wlan = network.WLAN(network.STA_IF)  # creates station interface
	wlan.active(True)                    # activates the interface

	if not wlan.isconnected():
		wlan.connect('SSID','PASSWORD') #connects to access point
		
		while not wlan.isconnected():
			pass

	ipAddress = wlan.ifconfig()   # gets the IP address, netmask, gateway, DNS
	global ip
	ip = ""
	ipAddr = ipAddress[:1] 
	for x in ipAddr:
		if x == "(":
			pass
		elif x == ")":
			pass
		elif x == ",":
			pass
		elif x == "'":
			pass
		else:
			temp = str(x)
			ip += temp  
	return ip


def disconnect():
	wlan.disconnect()
	print("Disconnecting....")
	wlan.active(False)
	print("Wifi Turned OFF")

