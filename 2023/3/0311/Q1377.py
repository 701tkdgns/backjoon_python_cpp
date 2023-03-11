import sys
input = sys.stdin.readline
N = int(input())
lst = [0 for i in range(N)]
ch = False
for i in range(N):
    lst[i] = int(input())

for i in range(N):
    ch = False
    for j in range(N - i - 1):
        if lst[j] > lst[j + 1]:
            ch = True
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
    if not ch:
        print(i + 1)
        break
