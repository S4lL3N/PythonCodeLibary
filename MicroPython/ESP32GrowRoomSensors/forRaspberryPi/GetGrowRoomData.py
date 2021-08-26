import gspread
from gspread import *
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


#########################################################################################################################################
plantData = "Plant#2"
#########################################################################################################################################

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("MicroPython\GRProject2\ForRaspPi\creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open(plantData).sheet1  # Open the spreadhseet
data = sheet.get_all_records()  # Get a list of all records

dayList = []
temperatureList = []
humidityList = []
soilMoistureList = []
soilRawList = []

def main():
    getLists()
    tempData = calculateHighLowAvg(temperatureList)
    humData = calculateHighLowAvg(humidityList)
    soilMoistData = calculateHighLowAvg(soilMoistureList)
    soilRawData = calculateHighLowAvg(soilRawList)

    days = calculateTotalDays(dayList)
    weeks = calculateTotalWeeks(days)

    temperatureMode = getModeAndCount(temperatureList)
    humidityMode = getModeAndCount(humidityList)
    soilMode = getModeAndCount(soilMoistureList)

    calculations = [tempData,humData,soilMoistData,days,weeks, temperatureMode, humidityMode, soilMode, soilRawData]

    #outputToConsole(calculations)
    writeToFile(calculations)
    #graphData("humidity", humidityList)

    #plt.plot(temperatureList, label="temp")
    #plt.plot(humidityList, label="Hum")
    #plt.legend()
    #plt.show()
    
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
        i += 1
        soilRaw = row.get('Soil Temperature(F)')
        if soilRaw != "":
            soilRawList.append(soilRaw)

def calculateHighLowAvg(dataList):
    try:
        i = 0
        total = 0
        lengthOfList = len(dataList)
        firstEntry = dataList[0]
        high = firstEntry
        low = firstEntry
        highPosition = 0
        lowPosition = 0
        while i < lengthOfList:
            entry = dataList[i]
            total += entry
            if entry > high:
                high = entry
                highPosition = i
            if entry < low:
                low = entry
                lowPosition = i
            i += 1
        avg = round(total / lengthOfList,2)
        results = [low, high, avg, lowPosition, highPosition]
    except Exception as e:
        print("Error...\n")
        print(e)
    return results

def calculateTotalDays(dayList):
    i = 0
    total = 1
    tempFirstDay = dayList[0] 
    temp = tempFirstDay.split(",")
    firstDay = temp[0]
    while i < len(dayList):
        tempDate = dayList[i]
        temp = tempDate.split(",")
        day = temp[0]
        if day != firstDay:
            total +=1
            firstDay = day
        i += 1
    totalDays = str(total)
    return totalDays

def calculateTotalWeeks(totalDays):
    tw = int(totalDays) / 7
    tw2 = round(tw,2)
    totalWeeks = str(tw2)
    return  totalWeeks

def getModeAndCount(dataList):
    tempMode = stats.mode(dataList)
    mode = tempMode[0]
    occured = tempMode[1]
    results = [mode, occured]
    return results

def getstandardDeviation(dataList):
    tempSTD = np.std(dataList) # standard devation 
    stdD = round(tempSTD,3)
    return stdD

def graphData(graphName, dataList):
    plt.plot(dataList)
    plt.ylabel(graphName)
    plt.show()
    '''
    #plot two lists
    plt.plot(temperatureList, label="temp")
    plt.plot(humidityList, label="Hum")
    plt.legend()
    plt.show()
    '''

def writeToFile(calculations):
    tempData = calculations[0]
    humData = calculations[1]
    soilMoistData = calculations[2]
    days = calculations[3]
    weeks = calculations[4]
    temperatureMode = calculations[5]
    humidityMode = calculations[6]
    soilMode = calculations[7]
    soilRawData = calculations[8]
    payload = str(plantData) + "\n\nTotal Days: " + days +"\nTotal Weeks: "+ weeks + "\n\nAverage Temperature: " + str(tempData[2]) +"\nAverage Humidity: " + str(humData[2]) +"\nAverage Soil Moisture: " + str(soilMoistData[2]) +'\n\nTemp Mode = ' + str(temperatureMode[0]) + " occured " + str(temperatureMode[1]) + " times" + '\nHumidity Mode = ' + str(humidityMode[0]) + " occured " + str(humidityMode[1]) + " times" +'\nSoil moisture Mode = ' + str(soilMode[0]) + " occured " + str(soilMode[1]) +  " times" + "\n\nHigh Temperature: " + str(tempData[1]) +"\nHigh Temperature Date: " + str(dayList[tempData[4]]) +"\n\nLow Temperature: "  + str(tempData[0]) +"\nLow Temperature Date: " + str(tempData[3]) +"\n\nHigh Humidity: " + str(humData[1]) +"\nHigh Humidity Date: " + str(dayList[humData[4]]) +"\n\nLow Humidity: "  + str(humData[0]) +"\nLow Humidity Date: " + str(dayList[humData[3]] + "\n\nHigh Soil Moist Raw: " + str(soilRawData[1]) + "\nLow Soil Moist Raw: " + str(soilRawData[0]))   
    f = open("GrowLog.txt", "w")
    f.write(payload)
    f.close()                  
    
def outputToConsole(calculations):
    tempData = calculations[0]
    humData = calculations[1]
    soilMoistData = calculations[2]
    days = calculations[3]
    weeks = calculations[4]
    temperatureMode = calculations[5]
    humidityMode = calculations[6]
    soilMode = calculations[7]
    soilRawData = calculations[8]
    print("\n\n")
    print(50 * "#")
    print(plantData)
    print(50 * "#")
    print("Total Days: " + days)
    print("Total Weeks: "+ weeks)
    print()
    print("Average Temperature: " + str(tempData[2]))
    print("Average Humidity: " + str(humData[2]))
    print("Average Soil Moisture: " + str(soilMoistData[2]))
    print()
    print('Temp Mode = ' + str(temperatureMode[0]) + " occured " + str(temperatureMode[1]) + " times")
    print('Humidity Mode = ' + str(humidityMode[0]) + " occured " + str(humidityMode[1]) + " times")
    print('Soil moisture Mode = ' + str(soilMode[0]) + " occured " + str(soilMode[1]) +  " times")
    print()
    print("High Temperature: "  + " High: " + str(tempData[1]))
    print("High Temperature Date: " + str(dayList[tempData[4]]))
    print()
    print("Low Temperature: "  + str(tempData[0]))
    print("Low Temperature Date: " + str(tempData[3]))
    print()
    print("High Humidity: " + str(humData[1]))
    print("High Humidity Date: " + str(dayList[humData[4]]))
    print()
    print("Low Humidity: "  + str(humData[0]))
    print("Low Humidity Date: " + str(dayList[humData[3]]))
    print()
    print("High Soil Raw:" + str(soilRawtData[1]))
    print("Low Soil Raw:" + str(soilRawData[0]))


main()
