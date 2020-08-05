number = input("input: ")
number = int(number)

for row in range(0, number, 1):
    for col in range(0, number - row, 1):
            print("*", end=" ")
    print("")
