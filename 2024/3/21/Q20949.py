import math

N = int(input())
ppi = []
for i in range(1, N + 1):
    W, H = map(int, input().split())
    ppi.append([math.sqrt(W * W + H * H) / 77, i])
ppi.sort(key=lambda x:x[0], reverse=True)

for p, i in ppi:
    print(i)
