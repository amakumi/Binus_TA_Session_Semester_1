print("")
print("Hollow pyramid of 5")
print("")
num = 5

for row in range(0, num, 1):
    for col in range(0, num, 1):
        if row + col == 2 or row - col == 2 or col - row == -2 or row + col == 6 or row - col == -2:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print("")
