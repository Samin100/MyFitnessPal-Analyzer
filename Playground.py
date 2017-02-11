import myfitnesspal
import datetime
import pprint
from datetime import datetime as dt
from datetime import timedelta


sharif = 'samin100'
issa = 'aladdin_heems'

client = myfitnesspal.Client(sharif)


def calculate_average_daily(nutrient, start_date, end_date):  # calories, carbohydrates, fat, protein, sodium, sugar

    # swaps dates if they were given backwards
    if start_date > end_date:
        start_date, end_date = end_date, start_date

    total = 0
    valid_days = 0

    while end_date > start_date:

        current_day = client.get_date(end_date)
        try:
            calories = current_day.totals['calories']
            if calories > 1500:
                total += current_day.totals[nutrient]
                valid_days += 1

        except KeyError:
            pass

        end_date -= timedelta(days=1)
    return round(total / valid_days)

def calculate_average_macro_ratio(start_date, end_date):
    # swaps dates if they were given backwards
    if start_date > end_date:
        start_date, end_date = end_date, start_date

    macro_totals = {'carbohydrates': 0, 'fat': 0, 'protein': 0}

    valid_days = 0

    while end_date > start_date:

        current_day = client.get_date(end_date)
        try:
            calories = current_day.totals['calories']
            if calories > 1500:
                print(end_date)
                macro_totals['carbohydrates'] += current_day.totals['carbohydrates']
                macro_totals['fat'] = current_day.totals['fat']
                macro_totals['protein'] = current_day.totals['protein']
                valid_days += 1
                pprint.pprint(macro_totals)

        except KeyError:
            pass

        end_date -= timedelta(days=1)

    final_macro_total = 0

    for key, value in macro_totals.items():
        final_macro_total += value

    print('Final macro total: ' + str(final_macro_total))


    macro_ratios = {'carbohydrates': 0, 'fat': 0, 'protein': 0}

    for key, value in macro_totals.items():
        print(key + ' ' + str(value))
        print(value / final_macro_total)



    pprint.pprint(macro_ratios)


# --------------------------------------Start of testing--------------------------------------

date1 = datetime.date.today() - timedelta(days=1)
date2 = datetime.date.today() - datetime.timedelta(days=7)
calculate_average_macro_ratio(date1, date2)

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

