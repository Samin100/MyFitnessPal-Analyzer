import Nutrition
from datetime import date, timedelta
import time
import myfitnesspal
from pprint import pprint

start = time.time()
samin = Nutrition.User(myfitnesspal.Client('samin100'))
print(samin)
print(samin.calculate_average_daily('carbohydrates', date.today(), date.today()))

