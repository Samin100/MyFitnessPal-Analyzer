import Nutrition
from datetime import date, timedelta
import time

start = time.time()

samin = Nutrition.User('samin100')
date1 = date.today() - timedelta(days=1)
date2 = date1 - timedelta(days=120)
print(samin.calculate_average_daily('protein', date1, date2))
end = time.time()
print('Completed: ' + str(end - start) + ' seconds')
