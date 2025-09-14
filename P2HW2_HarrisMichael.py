#Michael Harris
#September 13, 2025
#P2HW2
#Understanding List commands

#Create an empty list named "all_module_grades"
all_module_grades= []

#Prompt user to Enter grade for each module in a seperate statement
#Read grade and add to "all_module_grades"
all_module_grades.append(float(input(f"Enter grade for Module 1: ")))
all_module_grades.append(float(input(f"Enter grade for Module 2: ")))
all_module_grades.append(float(input(f"Enter grade for Module 3: ")))
all_module_grades.append(float(input(f"Enter grade for Module 4: ")))
all_module_grades.append(float(input(f"Enter grade for Module 5: ")))
all_module_grades.append(float(input(f"Enter grade for Module 6: ")))
#Display an empty line
print()

#Calculate "lowest_grade" as the minimum value in "all_madule_grades"
lowest_grade= min(all_module_grades)
#Calculate "highest_grade" as the maximum value in "all_madule_grades"
highest_grade= max(all_module_grades)
#Calculate "sum_of_grades" as the sum of values in "all_madule_grades"
sum_of_grades= sum(all_module_grades)
#Calculate "avg_grade" as the sum_of_grades divided by the number of elements in "all_madule_grades"
avg_grade= sum_of_grades / len(all_module_grades)

#Display "------------Results------------"
print("------------Results------------")
#Display "Lowest Grade: ", "lowest_grade"
print(f"Lowest Grade:\t", {lowest_grade})
#Display "highest Grade: ", "highest_grade"
print(f"Highest Grade:\t", {highest_grade})
#Display "Sum of Grades: ", "sum_of_grades"
print(f"Sum of Grades:\t", {sum_of_grades})
#Display "Average Grade: ", "avg_grade" formatted to two decimal places
print(f"Average:\t {avg_grade:.2f}")
#Display "----------------------------------------"
print("----------------------------------------")


