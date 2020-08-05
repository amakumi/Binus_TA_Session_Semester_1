num = (int(input("HOW MUCH?: ")))

for row in range(0, num, 1):
    for col in range(0, num, 1):
        if col < (num - row - 1):
            print(" ", end = "")
        else:
            print("* ", end = "")
    print("")
for row in range(num - 1, 0, -1):
    for col in range(0, num - row):
        print(" ", end = "")
    for col in range(0, row):
        print("* ", end = "")
    print("")