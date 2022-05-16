N, D = map(int, input().split())
arr = [[] for _ in range(10001)]
for _ in range(N):
    s, e, w = map(int, input().split())
distance = [i for i in range(D+1)]

for i in range(D + 1):
    if i != 0:
        distance[i] = min(distance[i], distance[i - 1] + 1)
    for w, e in arr[i]:
        if e <= D and w + distance[i] < distance[e]:
            distance[e] = w + distance[i]
print(distance[D])