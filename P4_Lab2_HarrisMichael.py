#Michael Harris
#September 29, 2025
#P4 LAB2
#Loops with integer multiplication, while and for loops together

'''
Get integer from user
Determine if integer is positive or negative
if number is positive, display multiplication table
if number is negative, tell user program cannot accept it
Ask user to run again?
If yes, run program
If no, end program
'''

run_again = 'yes'

#another option != "no":
while run_again == 'yes':

    user_num = int(input("Enter an integer: "))

    if user_num >= 0:
        #display multiplication for that value and range (1-12)
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")
    else:
        print("This program does not handle negative values")

    run_again = input("Woud you like to run the program again?")

#Loop has broke. User entered 'no'
print("Program is ending...")
    
