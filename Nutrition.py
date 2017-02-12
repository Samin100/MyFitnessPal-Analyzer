from datetime import timedelta
import myfitnesspal


class User(object):  # all (new) python classes inherit from the object class

    def __init__(self, username):  # constructor and instance variables
        """
        Constructor that takes a MFP client as a param.
        :param client: MFP.client client
        """
        self.username = username
        self.client = myfitnesspal.Client(username)
        self.MIN_CALORIE = 1000

    def calculate_average_daily(self, nutrient, start_date, end_date):
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

            current_day = self.client.get_date(end_date)
            try:
                calories = current_day.totals['calories']
                if calories > self.MIN_CALORIE:
                    total += current_day.totals[nutrient]
                    valid_days += 1

            except KeyError:
                pass

            end_date -= timedelta(days=1)
        return round(total / valid_days)

    def calculate_average_macro_ratio(self, start_date, end_date):
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

            current_day = self.client.get_date(end_date)
            try:
                calories = current_day.totals['calories']
                if calories > self.MIN_CALORIE:
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

    def find_day_max(self, nutrient, start_date, end_date):
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

            current_day = self.client.get_date(end_date)
            print()
            print(end_date)
            try:
                totals = current_day.totals
                print(totals)
                calories = totals['calories']
                if calories > self.MIN_CALORIE:
                    if totals[nutrient] > max_value:
                        max_value = totals[nutrient]
                        max_day = end_date

            except KeyError:
                pass

            end_date -= timedelta(days=1)

        return max_day
