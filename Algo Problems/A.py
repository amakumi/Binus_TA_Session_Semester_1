
def sword_art_online():
    s, n = map(int, input().split())
    a = []

    for i in range(n):
        a.append(list(map(int, input().split())))
    a.sort()

    for i in range(n):
        if s > a[i][0]:
            s += a[i][1]
        else:
            exit(print("NO"))

    print("YES")


sword_art_online()