"""Write a Python program to extract year, month, date and time using Lambda.
Sample Output:
2020-01-15 09:03:32.744178
2020
1
15
09:03:32.744178 """

import datetime

datetime_now = datetime.datetime.now()

year = lambda dt: dt.year
month = lambda dt: dt.month
date = lambda dt: dt.day
time = lambda dt: dt.strftime("%H:%M:%S.%f")

year = year(datetime_now)
month = month(datetime_now)
date = date(datetime_now)
time = time(datetime_now)

print(datetime_now)
print(year)
print(month)
print(date)
print(time)
