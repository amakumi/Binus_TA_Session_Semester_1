num = input("input: ")
num = int(num)

for row in range(0, num, 1):
    for col in range(0, num, 1):
        if col < (num - row - 1):
            print(" ", end = "")
        else:
            print("*", end = "")
    print("")

