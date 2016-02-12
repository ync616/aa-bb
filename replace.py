import sys
import datetime


now=datetime.datetime.now() 

nowDay=str(now.day)
nowHour=str(now.hour)
nowMinute=str(now.minute)

for line in sys.stdin:
	line = line.strip()
	line = line.replace("morning", "afternoon")
	line = line.replace("good", "bad")
	line = line.replace("four", nowHour+":"+nowMinute)
	line = line.replace("living", "coding")

	print line.title()

