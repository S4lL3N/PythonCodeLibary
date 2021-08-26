import gspread
from gspread import *
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint



#########################################################################################################################################
plantData = "Plant#2"
#########################################################################################################################################

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("MicroPython\GRProject2\ForRaspPi\creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open(plantData).sheet1  # Open the spreadhseet
data = sheet.get_all_records()  # Get a list of all records

soilRawList = []
convertedList = []

def main():
    getLists()
    i = 0 # 1st attemped ended at 66
    lengthOfList = len(soilRawList)
    f = open("converted.txt", "a")
    
      
    while i < lengthOfList:
        print(i)
        conversion = ChangeRange(soilRawList[i])
        convertedList.append(conversion)
        f.write(str(conversion) + "\n")
        i+=1
    #LogToSheet(convertedList)
    f.close()

def LogToSheet(converted):
    print("Logging to sheet")
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("TestSheet").sheet1  # Open the spreadhseet
    colLen=len(sheet.row_values(1))
    rowLen =len(sheet.col_values(1))
    insertRow = rowLen + 1 
    logData = [converted]
    sheet.insert_row(logData, insertRow)       

def ChangeRange(sensorReading):
    sensorRangeLow = 650
    sensorRangeHigh = 783
    newRangeHigh = 100
    newRangeLow = 0
    reading = (sensorReading - sensorRangeLow) / (sensorRangeHigh - sensorRangeLow) * (newRangeHigh - newRangeLow) + newRangeLow
    result = round(reading,2)
    return result

def getLists():
    i = 0
    lengthOfSheet =int(len(sheet.col_values(1))) -1
    f =open("soilRawData.txt", "a")
    while i < lengthOfSheet:
        row = data[i]
        soilRaw = row.get('Soil Temperature(F)')
        if soilRaw != "":
            soilRawList.append(soilRaw)
            f.write(str(soilRaw) + "\n")
        i += 1

main()