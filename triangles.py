
n = 0

print()
print("A")
print()
for i in range(0, 11):
    n = n + 1
    for j in range(0, n - 1):
        print("*", end = "")
    print()
print("")


print("B")
print()
for i in range(0, 11):
    n = n - 1
    for j in range(0, n + 1):
        print("*", end = "")
    print()
print("")


print ("C")
print()
for c in range (11, 0, -1):
    print((11 - c) * " " + c * "*")
print("")


print("D")
print()
for d in range (11, 0, -1):
    print(d * " " + (11 - d) * "*")
print("")


print("E")

print()

i = 1
j = 10
while i <= 10:
    print((j * " ") + i * "* ")
    j = j - 1
    i = i + 1

print("")

print()





