#!/usr/bin/python3

# key: value хандах боломжтой 
# tutorials = [name:'C', author:'C++', 'Python']

evekon = {'name': 'ErkhemBuyn', 'tutorial': 'Python'}
print(evekon['name'])

evekon = {
    'name': 'ErkhemBuyn',
    'tutorial': 'Python'
}

print(evekon['tutorial'])

evekon = {
    'name': 'ErkhemBuyn', 
    'tutorials': ['Python', 'C', 'C++', 'Java', 'Network']
}

print(evekon['tutorials'][0])
print(evekon['tutorials'][3])

print(evekon.get('name'))
print(evekon['name'])

print(dir(evekon))

print(evekon.items())
print(evekon.keys())
print(evekon.values())

evekon['name'] = 'Erhemee'
print(evekon['name'])

# del evekon['name']
# print(evekon)

# print(evekon['name'])
print(evekon.get('name'))
print(evekon.get('name', 'Not found'))
print(evekon.get('notthere', 'Key not found'))
print(evekon.get('notthere'))
print(evekon.get('notthere', 'Key not found'))
