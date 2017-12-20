#! /usr/bin/python3

import datetime 
import calendar

if __name__ == "__main__":
	now = datetime.datetime.now()
	cal = calendar.TextCalendar()
 	with open('cal.txt', mode='w') as file:
		file.write(cal.formatmonth(int(now.year),int(now.month)))
