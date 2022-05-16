N = int(input())
S = list(input())
res = 0

for i in range(N-1):
    if S[i] == 'E' and S[i+1] == 'W':
        res += 1
print(res)