from datetime import timedelta, datetime

given_date = datetime(2020, 3, 22, 10, 0, 0)
day_add = 7
res = given_date + timedelta(days=day_add, hours=12)
print(res)
