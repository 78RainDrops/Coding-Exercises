from datetime import datetime

date_string = "Feb 25 2020 4:20PM"
"""
%Y - Year
%m - Month
%d - day
%H - hour
%M - minutes
%S - seconds
"""
date_time = datetime.strptime(date_string, "%b %d %Y %I:%M%p")
print(date_time)
