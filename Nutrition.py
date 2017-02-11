import myfitnesspal


class User(object):  # all (new) python classes inherit from the object class

    def __init__(self, client):  # constructor and instance variables
        self.client = client
        self.min_threshold = 800
        self.username = client.effective_username

    def get_meals(self, days):
        return self.client


#  TODO: calculate_average function
#  TODO: max_day function
#  TODO: min_day function