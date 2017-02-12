import Nutrition
from datetime import date, timedelta
import time
import myfitnesspal
from pprint import pprint

start = time.time()
samin = Nutrition.User(myfitnesspal.Client('samin100'))

meals = samin.get_meals(date.today())
for meal in meals:
    print(meal + ': ')
    for item in meals[meal]:
        print(item['name'])
    print()

end = time.time()
print('Completed: ' + str(end - start) + ' seconds')
