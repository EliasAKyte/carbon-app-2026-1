efco2={'Bus':{'Diesel':0.035,'CNG':0.035,'Petrol':0.04,'Electric Europe':0.02},
  'Car':{'Petrol':0.140,'Diesel':0.145,'Electric Nordic':0.015, 'Electric Europe':0.045},
  'Plane':{'Petrol':0.24298},
  'Ferry':{'Diesel':0.130, 'CNG':0.110, 'Petrol':0.150},
  'Motorbike':{'Petrol':0.100 ,'Electric':0.015},
  'Scooter':{'No Fossil Fuel':0},
  'Bicycle':{'No Fossil Fuel':0},
  'Walk':{'No Fossil Fuel':0},
  'Train':{'Diesel':0.090,'Electric':0.007}
}

def carbon_emissions(kms, transport, fuel):
    co2=float(kms)*efco2[transport][fuel]
    return(co2)
