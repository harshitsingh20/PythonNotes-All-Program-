# json.loads()--------->  It is used to convert a json string to an dictonary
# json.dump()---------> It is used to convert a dictonary to an json string.

import json

data = '{"var1":"harshit", "var2":56}'
print(data)

parsed = json.loads(data)
print(type(parsed))

#Task 1 - json.load?


data2 = {
    "channel_name": "Ankit",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}

jscomp = json.dumps(data2)
print(jscomp)

# Task 2 = what is sort_keys parameter in dumps
