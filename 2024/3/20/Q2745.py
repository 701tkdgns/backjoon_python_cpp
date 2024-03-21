N, B = input().split()
N = ''.join(reversed(N))
B = int(B)
numCount = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
res = 0
for i in range(len(N)-1, -1, -1):
    res += numCount.index(N[i]) * (B**i)
print(res)
