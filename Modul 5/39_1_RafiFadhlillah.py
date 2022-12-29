#create a mapping of state to abbreviation
 states = {
'Indonesia': 'INA',
 'Jerman': 'GER',
 'Jepang': 'JPN',
 'Korea': 'KOR',
'Inggris': 'ING'
 }
#create a basic set of states and some cities in them
 cities = {
 'JKT': 'Jakarta',
 'TKY': 'Tokyo',
 'LDN': 'London'
 }

#add some more cities
cities['Berlin'] = 'BLN'
cities['Soul'] = 'SOU'
#print out some cities
 print('-' * 10)
print("Berlin State has: ", cities['BLN'])
print("Soul State has: ", cities['SOU'])
#print some states
print('-' * 10)
print("Indonesia abbreviation is: ", states['INA'])
print("Jepang abbreviation is: ", states['JPN'])
#do it by using the state then cities dict
print('-' * 10)
print("Indonesia has: ", cities[states['INA']])
print("Jepang has: ", cities[states['JPN']])
#print every state abbreviation
 print('-' * 10)
 for state, abbrev in list(states.items()):
 print(f"{state} is abbreviated {abbrev}")

#print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
print(f"{abbrev} has the city {city}")
#now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
print(f"{state} state is abbreviated {abbrev}")
print(f"and has city {cities[abbrev]}")
print('-' * 10)
#safely get a abbreviation by state that might not be there
state = states.get('China')
if not state:
print("Sorry, no China.")
#get a city with a default value
city = cities.get('CHN', 'Does Not Exist')
print(f"The city for the state 'CHN' is: {city}")