import gspread
from gspread import *
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from datetime import datetime

#print(data[0])
#row = data[0]
#print(row.get('Temperature(F)'))
#rowLen =int(len(sheet.col_values(1))) -1
#print(rowLen)
'''
{'Date And Time': 'April 1, 2020 at 12:16AM', 'Temperature(F)': 73.4, 'Humidity': 54, 'Soil Moisture': 80, 'Soil Temperature(F)': 58, 'Light Schedule ': 24, 'Water': '', 'Grow Big': '', 'Tiger Bloom': '', 'Big Bloom': '', 'PH': '', 'Stage': 'Seed'}
'''

#########################################################################################################################################
plantData = "Plant#2"
#########################################################################################################################################

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("GoogleSpreadSheetsAPI\creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open(plantData).sheet1  # Open the spreadhseet
data = sheet.get_all_records()  # Get a list of all records

dayList = []
temperatureList = []
humidityList = []
soilMoistureList = []
stageList = []
LightScheduleList = [] 

from scipy import stats 
import numpy
import matplotlib.pyplot as plt

def main():
    getLists()
    #twoDArray()
    #print("total cost = " +str(calculateElectricBill()))
    #print(timeInStage(dayList,stageList, "Seed"))
    #calculateTimeInStage(dayList)
    #tempSTD = numpy.std(temperatureList) # standard devation 
    #print(tempSTD)
    plt.plot(temperatureList)
    plt.ylabel('temperatures')
    plt.show()



def twoDArray():
    rows = int(len(sheet.col_values(1))) -1
    cols = int(len(sheet.row_values(1)))
    arr = [[0 for i in range(cols)] for j in range(rows)] 
    for row in arr: 
        print(row)


def getLists():
    i = 0
    lengthOfSheet =int(len(sheet.col_values(1))) -1
    while i < lengthOfSheet:
        row = data[i]
        temperature = row.get('Temperature(F)')
        if temperature != "":
            temperatureList.append(temperature)        
        humidity = row.get('Humidity')
        if humidity != "":
            humidityList.append(humidity)
        soilMoisture = row.get('Soil Moisture')
        if soilMoisture != "":
            soilMoistureList.append(soilMoisture)
        date = str(row.get('Date And Time'))
        dayList.append(date)
        stage = row.get('Stage')
        if stage != "":
            stageList.append(stage)
        lightSchedule = str(row.get('Light Schedule '))
        if lightSchedule != "":
            LightScheduleList.append(lightSchedule)
        i += 1

def calculateElectricBill():
    i = 0
    total = 1
    tempFirstDay = dayList[0] 
    temp = tempFirstDay.split(",")
    firstDay = temp[0]
    firstLightSch = LightScheduleList[0]
    t24H = 1
    t16H = 0
    t12H = 0

    while i < len(dayList):
        tempDate = dayList[i]
        temp = tempDate.split(",")
        day = temp[0]
        if day != firstDay:
            total +=1
            firstDay = day
            lightSch = LightScheduleList[i]
            #print(lightSch)
            if lightSch == "24":
                t24H += 1
            elif lightSch == "16":
                t16H += 1
            elif lightSch == "12":
                t12H += 1
        i += 1
    totalDays = str(total)
    seedlingCost = getCost(216,24,t24H)
    vegCost = getCost(600,16,t16H)
    flowerCost = getCost(600,12,t12H)
    totalCost = seedlingCost + vegCost + flowerCost
    return totalCost

def getCost(watts, hours, days):
    pricePerKWH = .09405 #april 2020
    kw = watts / 1000
    kwh = kw * hours
    costPerDay = pricePerKWH * kwh
    totalCost = costPerDay * days
    return totalCost
########################################################################################################################################
# still needs work
def timeInStage(dataList, stageList, stage):
    i = 0
    daysInStage = 0
    tempFirstDay = dayList[0] 
    temp = tempFirstDay.split(",")
    firstDay = temp[0]
    while i < len(dayList):
        tempDate = dayList[i]
        temp = tempDate.split(",")
        day = temp[0]
        currentStage = stageList[i]
    
        if day != firstDay and currentStage == stage:
            daysInStage +=1
            firstDay = day
        i += 1
    totalStageDays = str(daysInStage)
    
    stageData = totalStageDays
    return stageData


def calculateTimeInStage(dayList):
    formattedList = []
    i = 0
    while i < len(dayList):
        tempList = dayList[i].split()
        month = str(tempList[0])
        tempDay = str(tempList[1])
        day = str(tempDay[0])
        year = str(tempList[2])
        tempDate = month +" "+ day +", "+ year
        #print(tempDate)
        date = datetime.strptime(tempDate, '%B %d, %Y').strftime('%d/%m/%Y')
        print(date)
        #old_date = datetime.date(year, month, day)
        #formattedList.append(date)
        i += 1
        '''
    old_date = datetime.date(year, month, day)
    new_date = datetime.date.today()
    date_delta = new_date - old_date
'''
    
    #print(formattedList)
def TStage(dayList, stageList):
    tempDate = []
    tempStage = []
    stage_date = {} 
    for date in tempDate: 
        for value in tempStage: 
            stage_date[key] = value 
            tempStage.remove(value) 
            break 
    


main()