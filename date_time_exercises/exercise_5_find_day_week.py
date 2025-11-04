import calendar
from datetime import datetime

given_date = datetime(2020, 7, 26)

print(given_date.strftime("%A"))
print(given_date.today().weekday())

weekday = calendar.day_name[given_date.weekday()]
print(weekday)
weekday1 = given_date.today().weekday()
print(weekday1)
