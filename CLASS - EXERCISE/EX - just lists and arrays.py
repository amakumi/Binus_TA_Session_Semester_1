cars = ["BMW","Toyota","Mazda","Mitsubishi","Mercedes-Benz","Nissan","Honda"]

for z in cars:
    print("> ", z)

cars.append("Subaru")

print(len(cars))

print(cars)

cars[0] = "Rolls-Royce"

print(cars)

#----------------------------------------------------------------------------------
print("")
print("NUM 2: ")

cars1 = [["BMW","Toyota"],["Mazda"],["Mitsubishi","Mercedes-Benz"],["Nissan","Honda"]]


for i in cars1:
    for k in i:
        print(k, end = " ")
    print("")

print("NUM3: ")
print(cars1[2][1])
