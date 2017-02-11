import datetime
from datetime import datetime as dt
from datetime import timedelta

#  to be used as a test file for manipulating date-time objects

today = datetime.date.today()
print(today)
print(today.strftime('Today is %A %B %d, %Y'))

startDate = '12-01-2016'
endDate = '12-31-2016'

start = datetime.date.today()
end = start - timedelta(days=31)

while start > end:
    print(end)
    end += timedelta(days=1)