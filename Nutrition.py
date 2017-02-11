import myfitnesspal
import datetime
from datetime import datetime as dt
from datetime import timedelta


sharif = 'samin100'
issa = 'aladdin_heems'

client = myfitnesspal.Client(issa)


day = client.get_date(datetime.date.today())  # (year, month, day) format


# an example of accessing nutrition data with the API
print('Meals ate on ' + str(day.date) + '\n')

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

