# Employee Salary Generator

employee_name = "Raju"
basic_salary = 30000

# Allowances
hra = basic_salary * 20 / 100
da = basic_salary * 10 / 100

# Gross salary
gross_salary = basic_salary + hra + da

print("Employee Name:", employee_name)
print("Basic Salary:", basic_salary)
print("HRA:", hra)
print("DA:", da)
print("Gross Salary:", gross_salary)

# Bonus eligibility
if basic_salary >= 25000:
    bonus = 5000
else:
    bonus = 2000

print("Bonus:", bonus)

# Tax deduction
if gross_salary >= 35000:
    tax = gross_salary * 5 / 100
else:
    tax = 0

print("Tax Deduction:", tax)

# Net salary
net_salary = gross_salary + bonus - tax

print("Net Salary:", net_salary)

# Salary category
if net_salary >= 40000:
    print("Salary Category: High")
elif net_salary >= 30000:
    print("Salary Category: Medium")
else:
    print("Salary Category: Low")

# Logical operator
if net_salary > 30000 and bonus > 0:
    print("Employee has good salary package")
else:
    print("Salary package is average")
