import requests as req

#r = req.get("http://192.168.1.10:1880/ui/#/0", auth=("s4ll3n", "mangosgetyouhigher"))

r = req.get("http://192.168.1.10:1880/ledOFF", auth=("s4ll3n", "mangosgetyouhigher"), timeout=3)
print(r.text)
print(r.status_code)
#r.close

#garageDoor = req.post("http://192.168.1.10:1880/led2ON", auth=("s4ll3n", "mangosgetyouhigher"))
#print(garageDoor.status_code)


if r.status_code == 200:
    print("Turning Led ON...")
else:
    print(f'it failed and returned this:\n{r.status_code}\n and \n{r.text}')
    print(f"Failed...{r.status_code}")
