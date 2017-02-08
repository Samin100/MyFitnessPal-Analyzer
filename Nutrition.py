import myfitnesspal

client = myfitnesspal.Client('samin100')
day = client.get_date(2016, 12, 25)  # (year, month, day) format


# an example of accessing nutrition data with the API

print('Meals I ate on ' + str(day.date) + '\n')

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
