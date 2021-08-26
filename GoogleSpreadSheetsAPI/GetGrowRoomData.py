import gspread
from gspread import *
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


#########################################################################################################################################
plantData = "Plant#1"
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

def main():
    getLists()
    tempData = calculateHighLowAvg(temperatureList)
    humData = calculateHighLowAvg(humidityList)
    soilMoistData = calculateHighLowAvg(soilMoistureList)
    days = calculateTotalDays(dayList)
    weeks = calculateTotalWeeks(days)
    outputToConsole(tempData,humData,soilMoistData,days,weeks)
    

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

def outputToConsole(tempData,humData,soilMoistData,days,weeks):
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


main()