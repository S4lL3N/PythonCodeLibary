# docs.micropython.org/en/latest/esp32/quickref.html

#to call using the repl import file name (internet)
#EXAMPLE= import internet
#then type the file name and the function
#EXAMPLE= internet.connect()
import network 
ip = None

wlan = network.WLAN(network.STA_IF)  # creates station interface
wlan.active(True)

def connect(ssid, password):
	if not wlan.isconnected():
		wlan.connect(ssid,password) #connects to access point
		
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

def check():
	connected = wlan.isconnected()
	return connected


def disconnect():
	wlan.disconnect()
	print("Disconnecting....")
	wlan.active(False)
	print("Wifi Turned OFF")

