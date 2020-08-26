import json

data = {}
data['pers'] = []
data['pers'].append({
    'name': 'Sterling',
    'age': '30',
    'height': '180'
})
data['pers'].append({
    'name': 'Lana',
    'age': '30',
    'height': '190'
})
data['pers'].append({
    'name': 'Malory',
    'age': '50',
    'height': '170'
})

with open('pers.json', 'w') as outfile:
    json.dump(data, outfile)
