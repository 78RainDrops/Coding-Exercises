from datetime import datetime, timedelta

given_date = datetime(2020, 2, 25)

days_sub = 7

res_date = given_date - timedelta(days=days_sub)
print(res_date)
