#Michael Harris
#September 26, 2025
#P3HW1
#Debug


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = input('Enter grade for Module 1: ')
mod_2 = input('Enter grade for Module 2: ')
mod_3 = input('Enter grade for Module 3: ')
mod_4 = input('Enter grade for Module 4: ')
mod_5 = input('Enter grade for Module 5: ')
mod_6 = input('Enter grade for Module 6: ')

# add grades entered to a list

grades = mod_1, mod_2, mod_3, mod_4, mod_5, mod_6
numeric_grades = [int(grade) for grade in grades]

# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
total = sum(numeric_grades)
avg = total / len(grades)

# determine letter grade for average


if avg >= 90:
    print('Your grade is: A')
elif average >= 80:
    print('Your grade is: B')
elif average >= 70:
    print('Your grade is: C')
elif average >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F') 






