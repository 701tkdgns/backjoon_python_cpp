import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    lst = []
    for _ in range(N):
        r, c = map(int, input().split())
        lst.append([r, c])
    lst.sort(key=lambda x:(x[0], x[1]))
    cnt, stu = 0, N + 1
    for r, c in lst:
        if c < stu:
            cnt += 1
            stu = c
    print(cnt)