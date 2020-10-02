# Write a Python program to extract year, month, date and time using Lambda

import datetime
now=datetime.datetime.now()
print(now)
year=lambda x:x.year
month=lambda x:x.month
date=lambda x:x.day()
date=lambda x:x.date()
time=lambda x:x.time()

print(month(now))
print(year(now))
print(day(now))
print(date(now))
print(time(now))
