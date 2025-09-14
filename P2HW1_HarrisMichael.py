#Michael Harris
#September 13, 2025
#P2HW1
#Python basic calculations-better display

print("This program calculates and displays travel expenses")
print()

# get budget from user
budget=int(input("Enter Budget: "))
print()

# get destination from user
destination=input("Enter your travel destination: ")
print()

# get gas expenses from user
gas=int(input("How much do you think you will spend on gas? "))
print()

# get hotel expenses from user
hotel=int(input("Approximately, how much will you need for accomodation/hotel? "))
print()

# get food expenses from user
food=int(input("Last, how much do you need for food? "))
balance=budget - food - gas - hotel
print()


print("------------Travel Expenses------------")
print(f"Location:\t\t {destination:}")
print(f"Initial Budget:\t\t ${budget:.2f}")
print(f"Fuel:\t\t\t ${gas:.2f}")
print(f"Accomodation:\t\t ${hotel:.2f}")
print(f"Food:\t\t\t ${food:.2f}")
print("---------------------------------------")
print()
print(f"Remaining balance:\t ${balance:.2f}")