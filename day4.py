employee_name = "Raju"
basic_salary = 30000
working_days = 30
present_days = 27

# Salary deduction for absent days
if present_days < working_days:
    absent_days = working_days - present_days
    deduction = (basic_salary / working_days) * absent_days
    salary_after_deduction = basic_salary - deduction
else:
    salary_after_deduction = basic_salary

print("Salary after deduction =", salary_after_deduction)

# Bonus condition
if present_days >= 26:
    bonus = 3000
else:
    bonus = 1000

print("Bonus =", bonus)

# Final salary
final_salary = salary_after_deduction + bonus
print("Final Salary =", final_salary)

# Salary status
if final_salary >= 30000:
    print("Good Salary Package")
else:
    print("Average Salary Package")
