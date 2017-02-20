from pprint import pprint
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')

corolla = {
        'manufacturer': 'Toyota',
        'class': 'sedan',
        'designer':{
            'firstname': 'Atoyotoya',
            'surname': 'von Corolla'
        },
         'assembly':{
             'country': 'Japan',
             'city: ': 'Tokyo',
             'state': ''
         }}

db = client.examples
#db.autos.insert(corolla)


print('FOUND ONE')
pprint(db.autos.find_one({'manufacturer': 'Tesla Motors'}))