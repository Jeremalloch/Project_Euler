import datetime

__author__ = 'Jeremy Malloch'

total_sunday = 0
for year in range(1901, 2001):
    for month in range(1,13):
        if datetime.date(year, month, 1).strftime("%A") == "Sunday":
            total_sunday += 1

print("There are {} total Sundays".format(total_sunday))
