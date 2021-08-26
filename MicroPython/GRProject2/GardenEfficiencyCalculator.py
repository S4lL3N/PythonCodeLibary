'''
Grow Room Efficiency Calculator

You need figures for -

Total light wattage
Total flowering time in days
Light cycle hours
Total yield in grams

For example. A 600w HPS system used on a 12/12 hourly cycle in flowering for 60 days which produces 20ozs (560g) of dry bud.

1) Divide total lamp wattage by 1000 to get Kw/h.
600w/1000 = 0.6.

2) Multiply this figure by the hours of the light cycle.
0.6 x 12 = 7.2

3) Multiply this figure by the number of days in flowering.
7.2 x 60 = 432

4) Now divide the gram yield figure by the kilowatt figure.
560g / 432 = 1.29. That's 1.29g per K/w

453.6kwh- 600w 12h @ 63days/8weeks

Experienced growers should be shooting for a GE (Garden Efficiency) rating of 1.0, so anything over 1.0 is very good going.
'''

'''
https://www.brightridge.com/home-service/rates/

Date	Base Service	kWh Charge	FCA	DCRA	Total kWh Charge
April 2020	$21.00	$0.07384	$0.01521	$0.00500	$0.09405
March 2020	$21.00	$0.07594	$0.01731	$0.00264	$0.09589
February 2020	$21.00	$0.07594	$0.01741	$0.00500	$0.09835
January 2020	$21.00	$0.07594	$0.01949	$0.0039	$0.09933


https://www.inchcalculator.com/watts-to-kwh-calculator/

600w x 12h = 7.2kwh
600w x 20h = 12kwh
600w x 18h = 10.8kwh
600w x 16h = 9.6kwh

t5 54w per bulb x 4 = 216w
216w x 24h = 5.184kwh
216w x 18h = 3.888kwh
216w x 16h = 3.456kwh
'''
pricePerKWH = .09405
seedling = 21
veg = 42 # days = 6 weeks
flower = 63 #day = 9 weeks, 56 = 8 weeks
t5 = 216
mHHps = 600

def getCost(watts, hours, days):
    kw = watts / 1000
    kwh = kw * hours
    costPerDay = pricePerKWH * kwh
    totalCost = costPerDay * days
    return totalCost

seedlingPhase = getCost(t5,24,seedling)

print("seedling 24h with t5=" + str(getCost(t5,24,seedling)))
print("veg 16h with t5=" + str(getCost(t5,16,veg)))
print("veg 16h with MH=" + str(getCost(mHHps,16,veg)))
print("flower 12h with HPS=" + str(getCost(mHHps,12,flower)))