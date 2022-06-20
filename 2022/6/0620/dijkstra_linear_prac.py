def getsmallIndex():
    mn = inf
    idx = 0
    for i in range(n):
        if distance[i] < mn and not visit[i]:
            mn = distance[i]
            idx = i
    return idx


def dijkstra(start):
    visit[start] = True
    for i in range(n):
        distance[i] = lst[start][i]
    for i in range(n - 1):
        current = getsmallIndex()
        visit[current] = True
        for j in range(6):
            if distance[j] > distance[current] + lst[current][j]:
                distance[j] = distance[current] + lst[current][j]


n = 6
inf = 10 ** 10
lst = [
    [0, 2, 5, 1, inf, inf],
    [2, 0, 3, 2, inf, inf],
    [5, 3, 0, 3, 1, 5],
    [1, 2, 3, 0, 1, inf],
    [inf, inf, 1, 1, 0, 2],
    [inf, inf, 5, inf, 2, 0]
]

visit = [False] * n
distance = [0] * n

dijkstra(0)
print(*distance)
