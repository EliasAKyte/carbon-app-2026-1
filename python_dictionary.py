efco2={'Bus': 0.1,
  'Car': 0.2,
  'Plane': 0.3,
  'Ferry': 0.1,
  'Motorbike': 0.1,
  'Bicycle': 0,
  'Walk': 0 }
print(efco2)

print(efco2['Bus'])

efco2['Bus']=0.5
print(efco2['Bus'])
print(efco2)

del efco2['Bus']
print(efco2)

print(type(efco2))

efco2['Bus']={'Diesel':0.10231,'CNG':0.08,'Petrol':0.10231,'No Fossil Fuel':0}
print(efco2)

print(efco2['Bus']['Diesel'])

efco2={'Bus':{'Diesel':0.10231,'CNG':0.08,'Petrol':0.10231,'No Fossil Fuel':0},
  'Car':{'Petrol':0.18592,'Diesel':0.16453,'No Fossil Fuel':0},
  'Plane':{'Petrol':0.24298},
  'Ferry':{'Diesel':0.11131, 'CNG':0.1131, 'No Fossil Fuel':0},
  'Motorbike':{'Petrol':0.09816,'No Fossil Fuel':0},
  'Scooter':{'No Fossil Fuel':0},
  'Bicycle':{'No Fossil Fuel':0},
  'Walk':{'No Fossil Fuel':0},
  'Train':{'Diesel':0.035,'Electric':0}
}

print(efco2.get('Bus'))

print(efco2.items())
print(list(efco2.items()))
print(list(efco2.items())[0][0])
print(list(efco2.items())[0][1])

print(efco2.keys())

print(efco2.values())

for k, v in efco2.items():
  print(k, v)

for k1, v1 in efco2.items():
  for k2, v2 in efco2[k1].items():
    print(k1, v1) 
    print(k2, v2) 

