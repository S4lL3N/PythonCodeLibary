import datetime

formatHeader = "=" * 55
formatHeader2 = "=" * 20
print(formatHeader)
print(formatHeader2 + "Find 3 Paydays " + formatHeader2)
print(formatHeader + "\n")

year = str(datetime.datetime.today())
year = year.split("-")
year = year[0] + "-"



TempcheckTwo = str(input("Enter the start date of 2nd paycheck MM-DD: "))
checkTwo = year + TempcheckTwo
dateFormat = "%Y-%m-%d"
addDays = datetime.timedelta(days=28)
switchDate = datetime.timedelta(days=14)
counter = 1
savings = 0
threePayDay = 0
totalpay = 0

date2 =datetime.datetime.strptime(checkTwo,dateFormat)

ridgelineTotal = 2929.38 #12/10/19
acuraTotal = 1967.77 #12/10/19
acuraOff = ""
counter2 =0
tempAucra = 0
carPay= 222 + 157.80
futureSavings = 0
maxSavings = 0




while counter < 13:
	counter = counter +1
	payday = date2 + addDays
	tempPayday = str(payday)
	tempPayday = tempPayday.split(" ")
	tempPayday = tempPayday[0]
	#print(tempPayday)

	totalpay = totalpay + 3800
	savings = savings + 600
	futureSavings = futureSavings + carPay
	maxSavings = maxSavings + 335 # $420 paycheck 1 and $250 paycheck 2 divided by 2


	
	if acuraTotal > 222:
		acuraTotal = acuraTotal -222
		acuraOff = tempPayday
		
	ridgelineTotal = ridgelineTotal - 157.80

	date2 = payday
	

	# switchs payday #2 with payday#1 when all can go to savings
	temp = str(date2)
	temp = temp.split("-")
	temp = temp[2].split(" ")
	
	day = int(temp[0])
	if day < 7:
		tempA = str(payday)
		tempA = tempA.split(" ")
		tempA = tempA[0]
		print("\nAll to savings on: " + tempA)
		#print("Changing paydays")
		date2 = payday + switchDate
		savings = savings + 1400
		threePayDay = threePayDay + 1


futureSavings = futureSavings + savings

maxSavings = maxSavings + futureSavings

print("\nAll To Savings = " + str(threePayDay) + " times!")	

print("potental savings= ", str(savings))

print("\ntotal earned= ", str(totalpay))

print("\nRidgeline Bal = " + str(round(ridgelineTotal,2)))

print("Acura Bal = " + str(round(acuraTotal,2)) +"\t "+ acuraOff)

print("\nSavings without car payments: " + str(round(futureSavings,2)))
print("\nMax possible savings:  " + str(round(maxSavings,2)))
print("In "+ str(counter - 1) + " months")
print("\n\n")
