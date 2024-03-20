P, N = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
cnt = 0
for i in A:
    if P < 200:
        P += i
        cnt += 1
print(cnt)