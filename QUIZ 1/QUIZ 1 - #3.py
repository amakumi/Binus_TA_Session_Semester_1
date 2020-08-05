
quan = int(input("Input Quantity: "))
print("")

print("----------------------------------------------")

if quan >= 10 and quan <= 19:
    print(" You got 20% DISCOUNT!!!")
    print(" Total Price: $",quan * 99)
    print(" You saved: $", (99 * quan)* 0.2)
    print("")
    print(" YOU JUST HAVE TO PAY: $", ((quan * 99) - (99 * quan) * 0.2))

elif quan >= 20 and quan <= 49:
    print(" You got 30% DISCOUNT!!!")
    print(" Total Price: $", quan * 99)
    print(" You saved: $", (99 * quan)* 0.3)
    print("")
    print(" YOU JUST HAVE TO PAY: $", ((quan * 99) - (99 * quan) * 0.3))

elif quan >= 50 and quan <= 99:
    print(" You got 40% DISCOUNT!!!")
    print(" Total Price: $", quan * 99)
    print(" You saved: $", (99 * quan)* 0.4)
    print("")
    print(" YOU JUST HAVE TO PAY: $", ((quan * 99) - (99 * quan) * 0.4))

elif quan > 100:
    print(" You got 50% DISCOUNT!!!")
    print(" Total Price: $", quan * 99)
    print(" You saved: $", (99 * quan)* 0.5)
    print("")
    print(" YOU JUST HAVE TO PAY: $", ((quan * 99) - (99 * quan)* 0.5))

elif quan < 10:
    print(" Total Price: $", quan * 99)
    print(" :( --- NO DISCOUNT --- :(")

print("")
print(" HAPPY SHOPPING...")
print("----------------------------------------------")