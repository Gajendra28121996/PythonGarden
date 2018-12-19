
from datetime import date
from datetime import time
from datetime import datetime

today=date.today()
print(today)
print(date.today())
print(datetime.today())
print("Individual Date Components : "+str(today.day)+"/"+str(today.month)+"/"+str(today.year))
print("Today's Weekday # "+str(today.weekday()))
timestamp=datetime.now()
print(timestamp)