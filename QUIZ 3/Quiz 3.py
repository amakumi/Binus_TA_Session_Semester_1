from booksss import Books

master = {}


#FUNCTIONS
def read():
    file = open("book.txt", "r")
    for i in file:
        content = i.split("#")
        master[content[0]] = Books(content[0], str(content[1]),float(content[2]))

    file.close()

def write():
    temp = ""
    file = open("book.txt","w")
    for row in master.values():
        temp += master[row].title + "#" + master[row].author + "#" + master[row].price + "\n"

    file.write(temp)
    file.close()


def view():
    for row in master.values():
        print("----------------------------------------------------------")
        print("Title   : ",row.title)
        print("Author  : ",row.author)
        print("Price   : $",row.price)
        print("----------------------------------------------------------")
    sorted(master)


def new():
    name = input("Input Book Title [max 50 chars]: ")
    if len(name) > 50:
        print("BOOK TITLE TOO LONG")

    else:
        athr = str(input("Input Book Author: "))
        c = athr.split(" ")
        if len(c) > 1:
            athr = 0
            for i in range(0,len(c) - 1):
                athr = athr + 1

        prc = float(input("Input Book Price: "))
        if prc < 10.00:
            print("PRICE TOO CHEAP")
        elif prc > 999.99:
            print("PRICE TOO MUCH")
        else:
            d = Books(name, athr, prc)
            master[name] = d
            print("* * * * * * * * * * * * * *")
            print("Book Successfully Added..!")
            print("* * * * * * * * * * * * * *")


def remove():
    count = 0
    print("::            Librarypedia Remove Book")
    print("----------------------------------------------------------")
    view()

    athr = str(input("Input Author's Name to be removed:  "))
    x = []
    y = 0
    for athr in master.values():
        if athr == master[athr]:
            x.append(athr)
            y = 1
    if y:
        athr.view()
        yesno = input("Are you sure to remove this book? [ Y / N ] ")
        if yesno == "Y" or yesno == "y":
            del master[x[0]]
            print("     Success Removing Book!!")
        elif yesno == "N" or yesno == "n":
            print("ok")
            remove()
    else:
        print("     Whoops.. The specific book is NOT available")
        print("     You might check your spelling...")


def save_exit():
    temp = ""
    file = open("book.txt", "w")
    for row in master.values():
        temp += master[row].title + "#" + master[row].author + "#" + master[row].price + "\n"

    file.write(temp)
    file.close()
    print("     Thank You for Visiting Librarypedia...")


#USER INTERFACE

while 1:
    read()
    print("""

    ::                  Welcome Librarypedia
    ------------------------------------------------------------
    1. Insert New Book
    2. View All Book <Sort Ascending by Author>
    3. Remove Book
    4. Save and Exit Library

    """)
    selection = int(input("Choose > "))

    if selection == 1:
        new()

    elif selection == 2:
        view()

    elif selection == 3:
        remove()

    elif selection == 4:
        save_exit()
        break

    else:
        print("INVALID SYNTAX!")
