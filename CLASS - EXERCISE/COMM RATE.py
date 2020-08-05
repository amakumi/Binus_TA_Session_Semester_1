name = input("Name: ")
number = input("Number: ")
vol = input("Sales Vol.: $")
vol = float(vol)
number = int(number)

print("Name: ",name)
print("Number: ",number)
print("Sales Vol.: ",vol)

if vol > 0 and vol <= 200:
    print("Comm. rate: ", vol * 0.05)

elif vol > 200.01 and vol <= 1000:
    print("Comm. rate: ", ((200 * 0.05) + vol - 200) * 0.08)

elif vol > 1000.01 and vol <= 2000.01:
    print("Comm. rate: ", ((200 * 0.05) + (1200 - 200) * 0.08) + ((vol - 1000) * 0.1))

elif vol > 2000.01:
    print("Comm. rate: ", ((200 * 0.05) + ((1200 - 200) * 0.08) + ((2000 - 1000) * 0.1) + ((vol - 2000) * 0.12)))
