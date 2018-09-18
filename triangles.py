n = 0
print("A")
for i in range(0, 11):
    n = n + 1
    for i in range(0, n - 1):
        print("*", end = " ")
    print()
print("")


o = 0
print("B")
for i in range(n + 1, 1, -1):
    for o in range(i, 1, -1):
        print("*", end = " ")
    print()
print("")

e = 0
print ("C")
for e in range (11, 0, -1):
    print((11 - e) * " " + e * "*")
print("")

z = 0
print("D")
for z in range (11, 0, -1):
    print(z * " " + (11 - z) * "*")
print("")

