#Michael Harris
#September 30, 2025
#P4HW1
#Using loops

'''
Ask user to enter number of scores to be entered
Determine if each score entered is valid (0-100)
if score is not valid, ask for a VALID score
if score is valid, add score to a list
Display lowest score, score list after dropping lowest score, average of scores
Determine the letter grade for the average
'''

#Create an empty list named "all_module_grades"
all_module_grades= []

#Prompt user to enter the number of scores to be added
num_score = int(input("How many scores do you want to enter? "))
print()

while num_score >0:
    for score_grade in range(1, num_score+1):
        score = (float(input(f"Enter score #{score_grade}: ")))
        if 0 <= score <= 100:
            all_module_grades.append(score)
            num_score -= 1
        else:
            print()
            score = (float(input(f"INVALID score entered!!!!\nScore should be between 0 and 100\nEnter score #{score_grade} again: ")))
            if 0 <= score <= 100:
                all_module_grades.append(score)
            num_score -= 1
        


#Calculate lowest
lowest_grade= min(all_module_grades)
#Remove lowest score
modified_scores = all_module_grades
modified_scores.remove(lowest_grade)
#Calculate Sum of all grades
sum_of_grades = sum(modified_scores)
#Calculate average
avg_grade = sum_of_grades / len(modified_scores)
#Calculate letter grade
if avg_grade >= 90:
    grade = "A"
elif 80 <= avg_grade < 90:
    grade = "B"
elif 70 <= avg_grade < 80:
    grade = "C"
elif 60 <= avg_grade < 70:
    grade = "D"
elif avg_grade < 60:
    grade = "F"


#Display "-----------------Results-----------------"
print("-------------Results-------------")
#Display "Lowest grade"
print(f"Lowest Grade  :\t", lowest_grade)
#Display "Modified List"
print(f"Modified List :\t {modified_scores}")
#Display "Average Grade" formatted to two decimal places
print(f"Scores Average:\t {avg_grade:.2f}")
#Display Grade letter
print(f"Grade         :\t {grade}")
#Display "------------------------------------"
print("----------------------------------")
