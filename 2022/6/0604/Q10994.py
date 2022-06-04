import sys
sys.setrecursionlimit(100000)


def recursion(n):
    if n == 1:
        print('*')
        return

    for i in range(n*n):
        for j in range(n*n):
            recursion(i*j)


N = int(input())


# 1 : 1 * 1
# 2 : 5 * 5
# 3 : 9 * 9
# 4 : 13 * 13
