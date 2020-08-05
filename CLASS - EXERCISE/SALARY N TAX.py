salary = input("Input Salary: $")
salary = float(salary)

if salary <= 0 and salary < 4999.99:
    print("Your Income Tax:", salary * 0.05)
elif salary <= 5000 and salary < 9999.99:
    print("Your Income Tax:", salary * 0.1)
elif salary <= 10000 and salary < 19999.99:
    print("Your Income Tax:", salary * 0.15)
elif salary <= 20000 and salary < 29999.99:
    print("Your Income Tax:", salary * 0.2)
elif salary <= 30000 and salary < 39999.99:
    print("Your Income Tax:", salary * 0.25)
elif salary >40000:
    print("Your Income Tax:", salary * 0.3)



