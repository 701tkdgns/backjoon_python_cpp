import sys
input = sys.stdin.readline
N = int(input())
hq = []
res = [0 for _ in range(1000)]
for _ in range(N):
    hq.append(list(map(int, input().split())))

hq.sort(key=lambda x: -x[1])

for i in range(N):
    for j in range(hq[i][0] - 1, -1, -1):
        if res[j] == 0:
            res[j] = hq[i][1]
            break
print(sum(res))
