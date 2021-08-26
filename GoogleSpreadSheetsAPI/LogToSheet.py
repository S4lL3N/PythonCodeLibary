#Python\GoogleSpreadSheetsAPI\LogToSheet.py
import gspread
from gspread import *
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import datetime

def googleSheetsLog(whatOccured):
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("GoogleSpreadSheetsAPI\creds.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("TestSheet").sheet1  # Open the spreadhseet
    colLen=len(sheet.row_values(1))
    rowLen =len(sheet.col_values(1))
    insertRow =rowLen + 1
    x = datetime.datetime.now()
    #date = x.strftime("%Y,%m,%d,%I,%p")
    date = x.strftime("%x @ %I:%M:%S %p")
    logData = [date, whatOccured,"temp", "humidity", "soil temp","soil moisture"]
    sheet.insert_row(logData, insertRow) # Insert the list as a row at index 4