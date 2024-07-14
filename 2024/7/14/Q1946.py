import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    lst = []
    for _ in range(N):
        s, c = map(int, input().split())
        lst.append([s, c])
    lst.sort(key=lambda x: (x[0], x[1]))
    cnt, mx = 1, lst[0][1]
    for i in range(1, N):
        if mx > lst[i][1]:
            mx = lst[i][1]
            cnt += 1
    print(cnt)
