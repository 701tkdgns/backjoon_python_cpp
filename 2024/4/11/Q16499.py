alpha = dict()
N = int(input())
for _ in range(N):
    a = list(input().rstrip())
    a.sort()
    t = ''
    for i in a:
        t += i
    alpha[t] = 1
print(len(alpha.keys()))