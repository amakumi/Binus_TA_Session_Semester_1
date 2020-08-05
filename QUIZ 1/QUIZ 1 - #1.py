p = str(input("Input Symbol Character: "))
x = int(input("Input Number: "))

print("")

for row in range(0, x, 1):
    for col in range(0, x, 1):
        if row == col or (row == x - col - 1):
            print(p, end = "")
        else:
            print(" ", end = "")
    print("")
