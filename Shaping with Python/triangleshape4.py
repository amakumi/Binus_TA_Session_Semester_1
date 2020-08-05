num = int(input("HOW MUCH?: "))

for row in range(0, num, 1):
    for col in range(0, num, 1):
        if col < (num - row - 1):
            print("*", end = " ")
        elif col > (num - row - 1):
            print(" ", end = " ")
    print("")