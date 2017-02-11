import myfitnesspal
import datetime
import pprint
from datetime import datetime as dt
from datetime import timedelta


sharif = 'samin100'
issa = 'aladdin_heems'

client = myfitnesspal.Client(sharif)

def calculate_average_daily(type, start_date, end_date):

    # swaps dates if they were given backwards
    if start_date > end_date:
        start_date, end_date = end_date, start_date

    sumCalories = 0
    days = (end_date - start_date).days
    print(days)

    while end_date > start_date:

        print(end_date)
        end_date -= timedelta(days=1)


date1 = datetime.date.today() - timedelta(days=1)
date2 = datetime.date.today() - datetime.timedelta(days=30)
print(date1)
print(date2)
calculate_average_daily('calories', date1, date2)


quit()

day = client.get_date(datetime.date.today())  # (year, month, day) format


# an example of accessing nutrition data with the API
print('Meals ate on ' + str(day.date) + '\n')

calorie_total = client.get_date(datetime.date.today()).totals['calories']
print(calorie_total)

mealTypes = ['Breakfast', 'Lunch', 'Dinner', 'Snacks']
typeCount = 0
dayTotal = 0


for meal in day.meals:
    mealTotal = 0
    print(mealTypes[typeCount] + ': ')
    for entry in meal.entries:
        print(entry.name)  # entry.name gives us only the name of the food as a string, not it's nutritional data
        mealTotal += entry['calories']

    print('Meal total: ' + str(mealTotal) + ' calories\n')
    dayTotal += mealTotal
    typeCount += 1


print('Daily today: ' + str(dayTotal) + ' calories')

