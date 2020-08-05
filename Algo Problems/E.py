
def check(A, B):
    for i in A:
        for j in B:
            a = int(i) + int(j)
            if not str(a) in A and not str(a) in B:
                return i, j

def main():
    arr_a = int(input())
    A = input().split()

    arr_b = int(input())
    B = input().split()

    i, j = check(A, B)
    print(i, j)

#############################

main()


