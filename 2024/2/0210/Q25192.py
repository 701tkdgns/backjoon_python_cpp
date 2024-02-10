# import sys
# input = sys.stdin.readline
N = int(input())
lst = {}
cnt = 0
for _ in range(N):
    d = input()
    if d == "ENTER":
        lst = {}
    else:
        keys = lst.keys()
        if d not in keys:
            lst[d] = 1
            cnt += 1
print(cnt)
