import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
lst = []
for _ in range(N):
    tmp = list(map(str, input().split()))
    lst.append(tmp[1:])

lst.sort()
dash = '--'
answer = []
for i in range(N):
    if i == 0:
        for j in range(len(lst[i])):
            answer.append(dash * j_lst[i][j])
    else:
        idx = 0
        for j in range(len(lst[i])):
            if lst[i-1][j] != lst[i][j] or len(lst[i-1]) <= j:
                break
            else:
                idx = j + 1
        for j in range(idx, len(lst[i])):
            answer.append(dash * j + lst[i][j])
