from datetime import timedelta
import myfitnesspal
from pprint import pprint


class User(object):  # python classes inherit from the object class

    def __init__(self, client):  # constructor and instance variables
        """
        Constructor that takes a MFP client as a param.
        :param client: myfitnesspal client object
        """
        self.client = client
        self.MIN_CALORIE = 900


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

        if start_date == end_date:
            return self.client.get_date(start_date).totals[nutrient]

        total = 0
        valid_days = 0

        while end_date > start_date:

            current_day = self.client.get_date(end_date)
            try:
                calories = current_day.totals['calories']
                print()
                print(current_day)
                print(current_day.totals)
                if calories > self.MIN_CALORIE:
                    total += current_day.totals[nutrient]
                    valid_days += 1

            except KeyError:
                pass

            end_date -= timedelta(days=1)
        if valid_days > 0:
            return round(total / valid_days)
        else:
            return 0

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

    def get_meals(self, date):
        """
        Gets all the meals for a given date.
        :param date: datetime date object
        :return: dictionary of meals
        """

        day_meals = self.client.get_date(date).get_as_dict()
        return day_meals

    def get_nutrient_values(self, nutrient, start_date, end_date):
        """
        Generates a dictionary with the date being the key and the value being the nutrient value
        :param nutrient: should be one of the following strings: calories, carbohydrates, fat, protein, sodium, sugar
        :param start_date: must be a datetime date object
        :param end_date: must be a datetime date object
        :return: dictionary
        """

    def get_day(self, date):
        '''
        Returns a dictionary of meals from the start date to the end date.
        :param date: datetime date object
        :return: returns a dictionary in the form {meals: mealdata, totals: totaldata}
        '''

        return {'meals': self.get_meals(date), 'totals': self.client.get_date(date).totals}

