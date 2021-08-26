"""
from datetime import datetime, date
now = datetime. now()
current_time = now. strftime("%H:%M:%S")
today = datetime.today()
print("date=", today, "\tCurrent Time =", current_time)


# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)
# Textual month, day and year	
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)
# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)
# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)

"""



import datetime
u = datetime.datetime.strptime("2019-12-16","%Y-%m-%d")
d = datetime.timedelta(days=28)
t = u + d
print(t)
#####################################################################################################################################

print("\nFind 3 Paydays")

checkTwo = str(input("Enter the start date of 2nd paycheck YYYY-MM-DD: "))
dateFormat = "%Y-%m-%d"
addDays = datetime.timedelta(days=28)
switchDate = datetime.timedelta(days=14)
counter = 1
savings = 0
threePayDay = 0

date2 =datetime.datetime.strptime(checkTwo,dateFormat)


while counter < 13:
	counter = counter +1
	payday = date2 + addDays
	print(payday)
	date2 = payday
	savings = savings + 600
	temp = str(date2)
	temp = temp.split("-")
	temp = temp[2].split(" ")
	#print(day[0])
	day = int(temp[0])
	if day < 7:
		print("All to savings: " + str(payday))
		print("Changing paydays")
		date2 = payday + switchDate
		savings = savings + 1400
		threePayDay = threePayDay + 1

print("\nAll To Savings = " + str(threePayDay) + "")	
print("potental savings= ", str(savings))