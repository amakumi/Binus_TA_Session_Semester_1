#INITIAL CONDITIONS

master = [[""]*8 for row in range(0,8)]

x = 0
y = 0
import random
before = 0

def read():
    global before
    i = 0
    j = 0
    #global is to rationalize contents
    file = open("pokemon_map.txt", "r")
    for row in file:
        info = []
        info = row.split(" ") #split it
        if len(row) > 3:
            info[7] = int(info[7])
            info[7] = str(info[7])
            for j in range(0,len(info)):
                master[i][j] = info[j]
        else:
            before=info[0]
        i = i + 1
    file.close()

def edit():
    global x,y

    for row in range(0,8):
        for col in range(0,8):
            #EMPTY SPACES
            if master[row][col] == "0":
                print("o", end = " ")
            #INACCESSIBLE
            elif master[row][col] == "1":
                print("x", end = " ")
                x = row
                y = col
            #GRASS
            elif master[row][col] == "2":
                print("#", end = " ")
        print()
def write():
    file = open("pokemon_map.txt", "w")
    temp = ""
    for row in range(0,8):
        for col in range(0,8):
            temp = temp + master[row][col]
            #if it's on the edge of the printing space
            if row == 7:
                temp = temp + " "
            #add a new line
            if row > 7:
                temp = temp + "\n"

    file.close()

read()
#MENU
while 1:
    edit()
    print(x, y)#>>>ini apa?

    print("**********************")
    print("         MENU")
    print("**********************")
    print("[1] MOVE UP")
    print("[2] MOVE DOWN")
    print("[3] MOVE LEFT")
    print("[4] MOVE RIGHT")
    print("[5] SAVE and END GAME")

    selection = int(input("Select a number: "))

    if selection == 1:
        # to make sure the player don't go out of the map...
        if x != 0:
            #if player steps on a grass..!
            if (master[x - 1][y] == "2"):
                encounter = random.randint(0,1)#>>ini apa?
                if encounter == 1:
                    print("")
                    print("      ...AMBUSHHEDDD...     ")
                    print("  A WILD POKEMON APPEARED..!")
                    print("")
                #swapping and replacing
            master[x][y] = before
            x = x - 1
            before = master[x][y]
            master[x][y]= "1"
        else:
            print("INVALID MOVE..!")#if it does...

    elif selection == 2:
        # to make sure the player don't go out of the map...
        if x != 7:
            #if player steps on a grass..!
            if (master[x + 1][y] == "2"):
                encounter = random.randint(0,1)#>>ini apa?
                if encounter == 1:
                    print("")
                    print("      ...AMBUSHHEDDD...     ")
                    print("  A WILD POKEMON APPEARED..!")
                    print("")
                #swapping and replacing
            master[x][y] = before
            x = x + 1
            before = master[x][y]
            master[x][y] = "1"
        else:
            print("INVALID MOVE..!")#if it does...

    elif selection == 3:
        # to make sure the player don't go out of the map...
        if y != 0:
            #if player steps on a grass..!
            if (master[x][y - 1] == "2"):
                encounter = random.randint(0,1)#>>ini apa?
                if encounter == 1:
                    print("")
                    print("      ...AMBUSHHEDDD...     ")
                    print("  A WILD POKEMON APPEARED..!")
                    print("")
                #swapping and replacing
            master[x][y] = before
            y = y - 1
            before = master[x][y]
            master[x][y] = "1"
        else:
            print("INVALID MOVE..!")#if it does...

    elif selection == 4:
        # to make sure the player don't go out of the map...
        if y!=7:
            #if player steps on a grass..!
            if (master[x][y + 1] == "2"):
                encounter = random.randint(0,1)#>>ini apa?
                if encounter == 1:
                    print("")
                    print("      ...AMBUSHHEDDD...     ")
                    print("  A WILD POKEMON APPEARED..!")
                    print("")
                #swapping and replacing
            master[x][y] = before
            y = y + 1
            before = master[x][y]
            master[x][y] = "1"
        else:
            print("INVALID MOVE..1!")#if it does...
    else:
        print("INVALID COMMAND!")
