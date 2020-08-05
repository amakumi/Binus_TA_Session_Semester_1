from Student import Student

data = {}

def read():
    file = open("","r")
    for f in file:
        info = f.split(",")
        d = Student(info[0],int(info[1]),int(info[2]),int(info[3]))
        data[info[0]] = d

    file.close()

def view():
    print("||{:25}|{:5}|{:5}|{:5}||").format("NAME", "LST_SCORE", "RDG_SCORE", "ESS_SCORE")
    for row in data.values():
        print("||{:25}|{:5}|{:5}|{:5}||").format(row["NAME"], ["LST_SCORE"], ["RDG_SCORE"], ["ESS_SCORE"])

def new():
    name = input("Input name: ")
    if len(name) > 25:
        print("NAME TOO MUCH")
    else:

        lst = int(input("Input your LISTENING SCORE: "))
        if lst > 20 or lst < 0:
            print("INVALID SCORE")
        else:
                rdg = int(input("Input your READING SCORE: "))
                if rdg > 30 or rdg < 0:
                        print("INVALID SCORE")
                else:

                    ess = int(input("Input your ESSAY SCORE: "))
                    if ess > 25 or ess < 0:
                        print("INVALID SCORE")
                    else:
                        d = Student(name, listening, reading, score)
                        data(name) = d

def summary():
    for row in data.values():
        if l == 0:
            min = max = row.calcutate()
            total = row + 1.calculate()
            if min < row:
                min = row.calculate()
            if max < row.calculate():
                max = row.calculator()
            l = l + 1
    avg = total / len(data)
    print("MINIMUM SCORE: ",min)
    print("MAXIMUM SCORE: ",max)
    print("AVG SCORE: ",avg)

#MENU

read()
while 1:
    print("")
    print("'Smart English' Course Center")
    print("*******************************")
    print("1. Add new data")
    print("2. View data")
    print("3. View summary")
    print("4. Exit")
    print("")

    selection = int(input("Select a number: "))

    if selection == 1:
        print("Add new data")


    if selection == 2:
        print("View data")


    if selection == 3:
        print("View summary")
        print("")
        print("TOTAL DATA           :",)
        print("MAXIMUM SCORE        :",)
        print("MINIMUM SCORE        :",)
        print("AVG SCORE            :",)


    if selection == 4:
        print("EXIT, BYE.")
        break
    else:
        print("INVALID SYNTAX")
