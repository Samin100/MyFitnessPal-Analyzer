import myfitnesspal
import Nutrition
from datetime import date, timedelta
from pprint import pprint
from pymongo import MongoClient


client = MongoClient()
db = client.GainStats.users

samin = db.find_one({'username': 'samin100'})


pprint(samin['valid_value'])

