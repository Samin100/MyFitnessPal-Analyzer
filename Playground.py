import myfitnesspal
import datetime
import time
from pprint import pprint
from datetime import datetime as dt
from datetime import timedelta


sharif = 'samin100'
issa = 'aladdin_heems'
NUTRIENTS = ['calories', 'carbohydrates', 'fat', 'protein', 'sodium', 'sugar']
MIN_CALORIE = 1500  # a day must have more than this amount of calories to be counted as valid
print()

client = myfitnesspal.Client(sharif)


def calculate_average_daily(nutrient, start_date, end_date):
    """
    Calculates the daily average of a given nutrient across a date range.
    :param nutrient: should be one of the following strings: calories, carbohydrates, fat, protein, sodium, sugar
    :param start_date: must be a datetime date object
    :param end_date: must be a datetime date object
    :return: int
    """

    # swaps dates if they were given backwards
    if start_date > end_date:
        start_date, end_date = end_date, start_date

    total = 0
    valid_days = 0

    while end_date > start_date:

        current_day = client.get_date(end_date)
        try:
            calories = current_day.totals['calories']
            if calories > MIN_CALORIE:
                total += current_day.totals[nutrient]
                valid_days += 1

        except KeyError:
            pass

        end_date -= timedelta(days=1)
    return round(total / valid_days)


def calculate_average_macro_ratio(start_date, end_date):
    """
    Calculates the average macronutrient ratio across a date range.
    :param start_date: datetime date object
    :param end_date: datetime date object
    :return: a dictionary containing each macro's ratio
    """

    # swaps dates if they were given backwards
    if start_date > end_date:
        start_date, end_date = end_date, start_date

    macro_totals = {'carbohydrates': 0, 'fat': 0, 'protein': 0}
    valid_days = 0

    while end_date > start_date:

        current_day = client.get_date(end_date)
        try:
            calories = current_day.totals['calories']
            if calories > MIN_CALORIE:
                macro_totals['carbohydrates'] += current_day.totals['carbohydrates']
                macro_totals['fat'] += current_day.totals['fat']
                macro_totals['protein'] += current_day.totals['protein']
                valid_days += 1

        except KeyError:
            pass

        end_date -= timedelta(days=1)

    final_macro_total = 0

    for key, value in macro_totals.items():
        final_macro_total += value

    macro_ratios = {'carbohydrates': 0, 'fat': 0, 'protein': 0}
    completed_total = 0

    for key, value in macro_totals.items():
        macro_ratios[key] = round(100 * (value / final_macro_total))
        completed_total += macro_ratios[key]

    return macro_ratios


def find_day_max(nutrient, start_date, end_date):
    """
    Locates the day in a given range which has the max nutrient.
    :param nutrient: should be one of the following strings: calories, carbohydrates, fat, protein, sodium, sugar
    :param start_date: datetime date object
    :param end_date: datetime date object
    :return: a datetime date object
    """

    # swaps dates if they were given backwards
    if start_date > end_date:
        start_date, end_date = end_date, start_date

    max_value = -1
    max_day = 0

    while end_date > start_date:

        current_day = client.get_date(end_date)
        print()
        print(end_date)
        try:
            totals = current_day.totals
            print(totals)
            calories = totals['calories']
            if calories > MIN_CALORIE:
                if totals[nutrient] > max_value:
                    max_value = totals[nutrient]
                    max_day = end_date

        except KeyError:
            pass

        end_date -= timedelta(days=1)

    return max_day

def find_day_min(nutrient, start_date, end_date):
    """
    Locates the day in a given range which has the min nutrient.
    :param nutrient: should be one of the following strings: calories, carbohydrates, fat, protein, sodium, sugar
    :param start_date: datetime date object
    :param end_date: datetime date object
    :return: a datetime date object
    """

    # swaps dates if they were given backwards
    if start_date > end_date:
        start_date, end_date = end_date, start_date

    min_value = 9999999999
    min_day = 0

    while end_date > start_date:

        current_day = client.get_date(end_date)
        print()
        print(end_date)
        try:
            totals = current_day.totals
            print(totals)
            calories = totals['calories']
            if calories > MIN_CALORIE:
                if totals[nutrient] < min_value:
                    min_value = totals[nutrient]
                    min_day = end_date

        except KeyError:
            pass

        end_date -= timedelta(days=1)

    return min_day

# --------------------------------------Start of testing--------------------------------------

date1 = datetime.date.today() - timedelta(days=1)
date2 = datetime.date.today() - datetime.timedelta(days=14)
start = time.time()
bad_day = find_day_min('protein', date2, date1)
print(bad_day)
print(client.get_date(bad_day).totals)
end = time.time()
print('Timer: ' + str(end - start) + ' seconds')
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
