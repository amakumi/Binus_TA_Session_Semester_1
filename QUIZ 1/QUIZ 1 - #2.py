x = int(input("Input X: "))
y = int(input("Input Y: "))
temp = 1
z = 1

print("")

for i in range(0, y, 1):
    z = temp * x
    print(z, end = " ")
    temp = z