#Michael Harris
#September 13, 2025
#P2_Lab2
#Dictionary Code

vehicle_mpg = {
    "Camaro" : 18.21,
    "Prius" : 52.36,
    "Model S" : 110,
    "Silverado" : 26
}

keys = vehicle_mpg.keys()

print(keys)

select_vehicle = input("Enter a vehicle to see it's mpg: ")
mpg = vehicle_mpg[select_vehicle]
print(f"The {select_vehicle} gets {mpg}.")

miles = float(input(f"How many miles will you drive the {select_vehicle}? "))

gal_needed = miles/mpg 
print(f"{gal_needed:.2f} gallon(s) of gas are needed to drive the {select_vehicle} {miles} miles.")