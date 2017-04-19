import myfitnesspal
from datetime import datetime, timedelta

client = myfitnesspal.Client(username='samin100')

TIMEFRAME = 60  # numbers of days including today
CAL_THRESHOLD = 1000


curr = datetime.today()
calories = 0
valid_days = 0

for x in range(TIMEFRAME):  # 31 days (including today)

    try:
        calval = client.get_date(curr).totals['calories']
        print(str(curr.date().strftime('%m/%d/%y')) + ": " + str(calval))

        if int(calval) >= CAL_THRESHOLD:
            calories += calval
            valid_days += 1

    except KeyError:
        pass

    curr -= timedelta(days=1)


if valid_days > 0:
    avg_cal = calories / valid_days
    print("Average calories: " + str(avg_cal))
    print()
else:
    print("Not enough valid days")

