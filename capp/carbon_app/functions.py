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

def carbon_emissions(kms, transport, fuel):
    co2=float(kms)*efco2[transport][fuel]
    return(co2)
