#https://requests.readthedocs.io/en/master/user/authentication/

import requests as req


r = req.get("http://192.168.1.10:")
print(r)

#will print out everything you can do
#print(dir(r))

#prints out the html code
print(r.text)

#gets status code ie 200 or 401 ect
print(r.status_code)

#gets header info
print(r.headers)


#get request
payload = {'page':2, 'count':25}
getReq = req.get("https://httpbin.org/get", params=payload)
print(getReq.text)
print(r.url)

#posts data
sendData = {'username':'s4ll3n', 'password':'Mangosgetyouhigher'}
postData = req.post("https://httpbin.org/post", data=sendData)
#postData = req.post(("http://71.88.220.222:1880", sendData))
print(postData.text)

#gets the JSON data
print(postData.json())