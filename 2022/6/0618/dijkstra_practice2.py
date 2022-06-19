inf = 10 ** 10
n = 6
lst = [
    [0, 2, 5, 1, inf, inf],
    [2, 0, 3, 2, inf, inf],
    [5, 3, 0, 3, 1, 5],
    [1, 2, 3, 0, 1, inf],
    [inf, inf, 1, 1, 0, 2],
    [inf, inf, 5, inf, 2, 0]
]

visit = [False for _ in range(n)]
distance = [0 for _ in range(n)]


def getSmallIndex():
    mn = inf
    idx = 0
    for i in range(n):
        if distance[i] < mn and not visit[i]:
            mn = distance[i]
            idx = i
    return idx


def dijkstra(start):
    for i in range(n):
        distance[i] = lst[start][i]
    visit[start] = True
    for i in range(n - 1):
        current = getSmallIndex()
        visit[current] = True
        for j in range(6):
            if not visit[j]:
                if distance[current] + lst[current][j] < distance[j]:
                    distance[j] = distance[current] + lst[current][j]


dijkstra(0)
print(*distance)
