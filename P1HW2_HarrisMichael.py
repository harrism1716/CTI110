#Michael Harris
#September 5, 2025
#P1HW2
#Python basic calculations

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
print("Location:", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accomodation:", hotel)
print("Food:", food)
print()
print("Remaining balance:", balance)

