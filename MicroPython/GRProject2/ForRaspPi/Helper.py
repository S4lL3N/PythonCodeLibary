import datetime
from datetime import date

def calculateWeek(startDate):
    year = startDate[2]
    month = startDate[0]
    day = startDate[1]
    old_date = datetime.date(year, month, day)
    # New date example of "today"
    new_date = datetime.date.today()
    date_delta = new_date - old_date
    # date_delta is a "datetime.timedelta" object
    # "date_delta.days" gives an integer number of days
    #print("Days Between = %s" % date_delta.days)
    #print("Weeks Between = %s" % (date_delta.days/7.0))
    # related example, add 30 days to date
    #print("30 days from %s is %s" % \(new_date, new_date+datetime.timedelta(days=30) ))
    #print(int(date_delta.days/7.0))
    week = str(round(date_delta.days/7.0,2))
    if week == "0":
        week = "1"
    return week

def week(year, month, day):
    d1 = date(year,month,day)
    d2 = date.today()
    result = round((d2-d1).days/7,2)
    print(result)
    return result
