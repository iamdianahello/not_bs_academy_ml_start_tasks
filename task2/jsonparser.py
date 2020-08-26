import json

perslist = []

with open('pers.json') as json_file:
    data = json.load(json_file)

    for pers in data['pers']:
    	perslist.append('name: ' + pers['name'] + ', age: ' + pers['age'] + ', height: ' + pers['height'])
        
print(perslist)  
