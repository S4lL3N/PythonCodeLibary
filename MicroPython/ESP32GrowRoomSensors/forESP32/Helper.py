
'''
converts the the loop counter into H:MM format
'''
def countToTime(count):
    temp = (count * 10) / 60
    if temp > 120:
        hours = 2
        mins = temp - 120
        time = str(hours) + ":" + str(int(mins))
    elif temp > 60:
        hours = 1
        mins = temp - 60
        time = str(hours) + ":" + str(int(mins))
    else:
        hours = 0
        mins = temp
        time = str(hours) + ":" + str(int(mins))
    
    return time


'''
to change the range of the soil moisture sensor from what it is to 0-100
example: range of 300-500 to 0-100
Result := ((Input - InputLow) / (InputHigh - InputLow))
          * (OutputHigh - OutputLow) + OutputLow;
case:
Result := ((Input - 300) / (500 - 300) * (100 - 0) + 0;
ChangeRange(300,500,0,100,450)
'''
def ChangeRange(sensorRangeLow, sensorRangeHigh, sensorReading):
    newRangeHigh = 100
    newRangeLow = 0
    reading = (sensorReading - sensorRangeLow) / (sensorRangeHigh - sensorRangeLow) * (newRangeHigh - newRangeLow) + newRangeLow
    result = round(reading,2)
    return result
