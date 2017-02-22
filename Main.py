import myfitnesspal
import Nutrition
from datetime import date, timedelta
from pprint import pprint
from pymongo import MongoClient

client = myfitnesspal.Client('samin100')
user = Nutrition.User(client)

pprint(user.get_day(date.today() - timedelta(days=1)))


client = MongoClient()
db = client.GainStats.users


print(db.find_one({'username': 'samin100'}))

