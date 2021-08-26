import gspread
from gspread import *
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import datetime
import Helper

#######################################################################################################################################
startDate = [5,7,2020]
startDay = 7 
startMonth = 5
startYear = 2020
#weekTotal = str(Helper.week(startYear,startMonth,startDay))
#----------------------
#lightSchedule = "24"
#lightSchedule = "20/4"
lightSchedule = "18/6"
#lightSchedule = "12/12"
#----------------------
growthStageStr = "Veg Week: "
#growthStage = "Seedling Week: "+ weekTotal
#growthStage = "Seedling Week: "+ Helper.calculateWeek(startDate)
#growthStage = "Veg Week: "+ Helper.calculateWeek(startDate)
#growthStage = "Flower Week: "+ Helper.calculateWeek(startDate)
#######################################################################################################################################

def googleSheetsLog(temp, humidity, soilMoisture, soilTemp, plant):
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    if plant == 'Plant#1':
        sheet = client.open(plant).sheet1  # Open the spreadhseet
    elif plant == 'Plant#2':
        sheet = client.open(plant).sheet1  # Open the spreadhseet
    elif plant == 'Plant#3':
        sheet = client.open(plant).sheet1  # Open the spreadhseet
    elif plant == 'Plant#4':
        sheet = client.open(plant).sheet1  # Open the spreadhseet

    #sheet = client.open("GDP#2").sheet1  # Open the spreadhseet
    colLen=len(sheet.row_values(1))
    rowLen =len(sheet.col_values(1))
    insertRow = rowLen + 1

    x = datetime.datetime.now()
    #date = x.strftime("%Y,%m,%d,%I,%p")
    #date = x.strftime("%x @ %I:%M:%S %p") # 04/02/20 @ 12:07:01 PM
    date = x.strftime("%B %-d, %Y @ %I:%M %p") # April 2, 2020 @ 12:29 PM

    water = ""
    GB = ""
    TB = ""
    BB = ""
    PH = ""

    d1 = datetime.date(startYear,startMonth,startDay)
    d2 = datetime.date.today()
    result = (d2 -d1).days/7
    rResult = round(result,2)
    growthStage = growthStageStr + str(rResult)

    #logData = [date, temp, humidity, soilMoisture, soilTemp]
    logData = [date, temp, humidity, soilMoisture, soilTemp, lightSchedule, water, GB,TB,BB,PH, growthStage]
    sheet.insert_row(logData, insertRow) # Insert the list as a row at index 4

