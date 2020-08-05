gpa = input("input gpa: ")
gpa = float(gpa)

if gpa >= 3.5 and gpa<=4.0:
 print("Cumlaude")
elif gpa >= 3.0 and gpa < 3.5:
 print("Outstanding")
elif gpa >= 2.5 and gpa < 3.0:
 print("Very Good")
elif gpa >= 2.0 and gpa < 2.5:
 print("Good")
elif gpa <2.0 and gpa >= 2.0:
 print("Poor")
elif gpa >4.0:
 print("THIS IS NOT A GPA!")
else:
 print("wrong input, try again fella...")