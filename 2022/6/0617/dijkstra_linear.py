# #linear
#
# def getSmallIndex():
#     mn = INF
#     index = 0
#     for i in range(N):
#         if distance[i] < mn and not visit[i]:
#             mn = distance[i]
#             index = i
#     return index
#
#
# def dijkstra(start):
#     for i in range(N):
#         distance[i] = lst[start][i]
#     visit[start] = True
#     for i in range(N - 1):
#         current = getSmallIndex()
#         visit[current] = True
#         for j in range(6):
#             if not visit[j] and distance[current] + lst[current][j] < distance[j]:
#                 distance[j] = distance[current] + lst[current][j]
#
#
# N = 6
# INF = 10000000000
#
# lst = [
#     [0, 2, 5, 1, INF, INF],
#     [2, 0, 3, 2, INF, INF],
#     [5, 3, 0, 3, 1, 5],
#     [1, 2, 3, 0, 1, INF],
#     [INF, INF, 1, 1, 0, 2],
#     [INF, INF, 5, INF, 2, 0],
# ]
#
# for i in range(N):
#     visit = [False for _ in range(N)]
#     distance = [0 for _ in range(N)]
#     dijkstra(i)
#     print(*distance)



# 내용 이해 체크
# 간선에 대해 최소값을 구한다
# 현재 값과 최소값과 비교하여 갱신한다.


def getSmallIndex():
    mn = INF
    idx = 0
    for i in range(n):
        if D[i] < mn and not visit[i]:
            mn = D[i]
            idx = i
    return idx


def dijkstra(start):
    for i in range(n):
        D[i] = lst[start][i]
    visit[start] = True
    for i in range(n - 1):
        current = getSmallIndex()
        visit[current] = True
        for j in range(n):
            if not visit[j] and D[current] + lst[current][j] < D[j]:
                D[j] = D[current] + lst[current][j]


n = 6
INF = 10**10
lst = [
    [0, 2, 5, 1, INF, INF],
    [2, 0, 3, 2, INF, INF],
    [5, 3, 0, 3, 1, 5],
    [1, 2, 3, 0, 1, INF],
    [INF, INF, 1, 1, 0, 2],
    [INF, INF, 5, INF, 2, 0],
]

for i in range(n):
    visit = [False for _ in range(n)]
    D = [0 for _ in range(n)]
    dijkstra(i)
    print(*D)
