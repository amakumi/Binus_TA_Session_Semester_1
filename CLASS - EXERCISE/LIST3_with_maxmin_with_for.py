print("")
n = int(input("How Many Num: "))
arr = [0] * n

print("")
print("ARRAY: ")

for i in range(0, n):
    arr[i] = int(input("List Your Num: "))

print("")
print(arr)

min = arr[0]
for i in range(1, n):
    if arr[i] > min:
        min = arr[i]

max = arr[0]
for i in range(1, n):
    if arr[i] < max:
        max = arr[i]

print("Min: ", min)
print("Max: ", max)