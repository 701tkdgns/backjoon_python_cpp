import sys
input = sys.stdin.readline
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    else:
        cnt = 0
        cd = dict()
        for _ in range(n + m):
            idx = int(input())
            cd[idx] = cd.get(idx, 0) + 1
        keys = cd.keys()
        for key in keys:
            cnt = cnt + 1 if cd[key] == 2 else cnt
        print(cnt)