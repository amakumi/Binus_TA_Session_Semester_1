

def death_note():
    first_input = input().split()
    num_days = int(first_input[0])
    max_names = int(first_input[1])

    e = 0
    second_input = input().split()

    ans = []

    for i in range(num_days):
        ans.append(int(second_input[i]))

    for i in range(num_days):
        ans[i] = ans[i] + e
        d = ans[i] // max_names
        print(d)
        e = ans[i] % max_names

#######################################

death_note()
