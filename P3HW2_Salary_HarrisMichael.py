#Michael Harris
#September 26, 2025
#P3_HW2
#Salary

name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

#hours of overtime
if hours_worked > 40:
    overtime = hours_worked - 40
else:
    overtime = 0

#calculate overtime pay
if hours_worked > 40:
    overtime_pay = pay_rate * 1.5 * overtime
else:
    overtime_pay = 0

#calculate regular pay
if hours_worked > 40:
    regtime = 40
else:
    regtime = hours_worked

reghour_pay = regtime * pay_rate

#calculate gross pay
if hours_worked > 40:
    gross_pay = overtime_pay + reghour_pay
else:
    gross_pay = reghour_pay

#Final output
print("-------------------------------------")
print("Employee name: ", name)
print()
print("Hours Worked     Pay Rate    OverTime    OverTime Pay    RegHour Pay     Gross Pay")
print("------------------------------------------------------------------------------------------------")
print(f'{hours_worked:<16.1f} {pay_rate:<11.1f} {overtime:<11.1f} {overtime_pay:<15.2f} ${reghour_pay:<14.2f} ${gross_pay:.2f}')