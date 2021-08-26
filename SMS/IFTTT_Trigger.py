import requests as req

#will send a text to my phone using IFTTT smooths4ll3n Account
# using the webhooks request in IFTTT
#https://ifttt.com/applets/107905018d
#req.post("https://maker.ifttt.com/trigger/Python_Script/with/key/fn0wxvll25ufUBqHS4PhRZ9j9KwWjgG59hnKzSaHQwn")

"""
webhooks key:
    Your key is: fn0wxvll25ufUBqHS4PhRZ9j9KwWjgG59hnKzSaHQwn

    example url:
        https://maker.ifttt.com/trigger/{event}/with/key/fn0wxvll25ufUBqHS4PhRZ9j9KwWjgG59hnKzSaHQwn
        https://maker.ifttt.com/trigger/Python_Script/with/key/fn0wxvll25ufUBqHS4PhRZ9j9KwWjgG59hnKzSaHQwn

    Event Name: Python_Script
"""

import requests

def SMS_alert(first, second, third):
    report = {}
    report["value1"] = first
    report["value2"] = second
    report["value3"] = third
    req.post("https://maker.ifttt.com/trigger/Python_Script/with/key/fn0wxvll25ufUBqHS4PhRZ9j9KwWjgG59hnKzSaHQwn", data=report)  
    #req.post("https://maker.ifttt.com/trigger/DHT11_Readings/with/key/fn0wxvll25ufUBqHS4PhRZ9j9KwWjgG59hnKzSaHQwn", data=report)   

print("Choose your first string.")
a = input()
print("Choose your second string.")
b = input()
print("Choose your third string.")
c = input()
SMS_alert(a, b, c)