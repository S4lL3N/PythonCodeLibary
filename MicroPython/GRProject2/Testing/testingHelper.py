import requests
import datetime


def postToSheets():
    temp = 70
    hum = 50
    soilMoist = 80
    soilTemp = str(65)
    request_headers = {'Content-Type': 'application/json'}
    #res = urequests.post('http://192.168.1.10:4200/api/sensor_readings', json={"temp":"70", "hum":"49","soilMoist":"80","soilTemp":"58"})
    res = requests.post('http://192.168.1.10:4200/api/sensor_readings', json={"temp":temp, "hum":hum,"soilMoist":soilMoist,"soilTemp":soilTemp}, headers=request_headers)
    if res.ok:
        #print(res.json())
        print("Request was successful")
    else:
        print("***FAILED***")


def SMS_alert_IFTTT(plant, soilMoisture):
    report = {}
    report["value1"] = plant
    report["value2"] = soilMoisture
    request_headers = {'Content-Type': 'application/json'}
    request = requests.post('https://maker.ifttt.com/trigger/GR_SMS/with/key/fn0wxvll25ufUBqHS4PhRZ9j9KwWjgG59hnKzSaHQwn',
    json=report,
    headers=request_headers)
    #print(request.text)
    request.close()


def ChangeRange(OrigLOW, OrigHIGH, NewLOW, NewHigh, Reading):
    result = (Reading - OrigLOW) / (OrigHIGH - OrigLOW) * (NewHigh - NewLOW) + NewLOW
    print(result)
    return result

import datetime
# takes date in month, day, year format mm,dd,yyyy
def calculateWeek(startDate):
    year = startDate[2]
    month = startDate[0]
    day = startDate[1]
    old_date = datetime.date(year, month, day)
    # New date example of "today"

    new_date = datetime.date.today()
    date_delta = new_date - old_date

    # date_delta is a "datetime.timedelta" object
    # "date_delta.days" gives an integer number of days
    #print("Days Between = %s" % date_delta.days)
    #print("Weeks Between = %s" % (date_delta.days/7.0))
    # related example, add 30 days to date
    #print("30 days from %s is %s" % \(new_date, new_date+datetime.timedelta(days=30) ))

    #print(int(date_delta.days/7.0))
    week = str(round(date_delta.days/7.0,2))
    if week == "0":
        week = "1"

    return week

def loop():
    i=0
    while i < 10:
        print(i)
        i+=1
loop()
#SMS_alert_IFTTT("GDP#2",20)
#ChangeRange(300,500,0,100,450)
#postToSheets()

