import gspread
from gspread import *
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("Python\GoogleSpreadSheetsAPI\creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("TestSheet").sheet1  # Open the spreadhseet

data = sheet.get_all_records()  # Get a list of all records


row = sheet.row_values(3)  # Get a specific row
col = sheet.col_values(3)  # Get a specific column
cell = sheet.cell(1,2).value  # Get the value of a specific cell


insertRow = ["hello","this","is","a","test"]
sheet.insert_row(insertRow, 4) # Insert the list as a row at index 4

sheet.update_cell(2,2, "test")  # Update one cell

numRows = sheet.row_count  # Get the number of rows in the sheet


#gets the dimentions of the rows and cols to determine when to insert data
colLen=len(sheet.row_values(1))
rowLen =len(sheet.col_values(1))
print('column count',end=' ')
print(colLen)
print('row count',end=' ')
print(rowLen)
