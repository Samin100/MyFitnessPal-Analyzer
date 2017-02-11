import myfitnesspal


class User(object):

    def __init__(self, client):
        self.client = client

    def get_meals(self, days):
        return self.client


if __name__ == '__main__':
    print('hi')