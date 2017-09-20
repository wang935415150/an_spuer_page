from datetime import datetime
from datetime import date
import json


class JsonCustomEncoder(json.JSONEncoder):
    def default(self, field):
        if isinstance(field, datetime):
            return field.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(field, date):
            return field.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, field)

data_list = [
    {'name':'alex','age':19, 'ctime': datetime.now()},
    {'name':'egon','age':19, 'ctime': datetime.now()},
    {'name':'eric','age':19, 'ctime': datetime.now()},
    {'name':'rain','age':19, 'ctime': datetime.now()}
]

val = json.dumps(data_list,cls=JsonCustomEncoder)
print(val)