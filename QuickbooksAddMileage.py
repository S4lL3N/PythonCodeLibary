from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time
import datetime
from datetime import timedelta  
import calendar 

startDate = datetime.date(2020, 4, 16) #4/16/20 the last day I logged
endDate = '2020-12-31'
MTWMiles = 233
TFMiles = 205
keyboard = KeyboardController()
mouse = MouseController()

# https://selfemployed.intuit.com/home#/app/mileagelog
# works on lenov04/27/2020eString(date): 
    temp = date.split("-")
    formattedDate = temp[1]+"/"+temp[2]+"/"+temp[0] 
    return formattedDate

def addMiles():
    counter = 1
    while True:
        nextDay = startDate + timedelta(days=counter)
        strNextDate = str(nextDay)
        date = changeDateString(strNextDate)
        day = findDay(nextDay)
        miles = ''
        f = open("MileageLog.txt", "a")
     
        if day == "Monday":
            miles =str(MTWMiles)
            logToQB(date, miles)
        elif day == "Tuesday":
            miles =str(MTWMiles)
            logToQB(date, miles)
        elif day == "Wednesday":
            miles =str(MTWMiles)
            logToQB(date, miles)
        elif day == "Thursday":
            miles =str(TFMiles)
            logToQB(date, miles)
        elif day == "Friday":
            miles =str(TFMiles)
            logToQB(date, miles)
        else:
            pass

        payload="Logged Mileage for " + date + " Miles=" + miles + "\n"
        f.write(payload)
        f.close() 

        if strNextDate == endDate:
            print("Done!")
            break

        counter +=1
        time.sleep(2)
        
def timer(seconds):
    counter = seconds
    while counter > 0:
        time.sleep(1)
        print(counter)
        counter-=1

def getMousePosition():
    print('The current pointer position is: {0}'.format(mouse.position))
    # Quickbooks website mouse positions for the Lenovo Laptop
    # Add Trip button position is: (1375, 204)
    # date texbox position is: (356, 582)
    # Miles texbox position is: (1108, 586)
    # Trip purpose texbox position is: (947, 708)
    # Save Button position is: (1367, 788)
 
def findDay(date): 
    temp = str(date)
    temp2 = temp.split("-")
    temp3 = temp2[0] + " " + temp2[1] + " " + temp2[2]
    weekday = datetime.datetime.strptime(temp3,'%Y %m %d' ).weekday()
    return (calendar.day_name[weekday]) 
  
main()





