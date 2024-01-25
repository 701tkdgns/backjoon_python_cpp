# import heapq as hq
#
# V, E = map(int, input().split())
# graph = [[] for _ in range(V + 1)]
# dist = [[1e9] * (V + 1) for _ in range(V + 1)]
#
# heap = []
# for _ in range(E):
#     x, y, c = map(int, input().split())
#     graph[x].append([c, y])
#     dist[x][y] = c
#     hq.heappush(heap, [c, x, y])
#
# while heap:
#     d, s, g = hq.heappop(heap)
#     if s == g:
#         print(d)
#         break
#     if dist[s][g] < d:
#         continue
#
#     for nd, ng in graph[g]:
#         new_d = d + nd
#         if new_d < dist[s][ng]:
#             dist[s][ng] = new_d
#             hq.heappush(heap, [new_d, s, ng])
# else:
#     print(-1)


V, E = map(int, input().split())
matrix = [[int(1e9)] * (V+1) for _ in range(V+1)]
for _ in range(E):
    x, y, c = map(int, input().split())
    matrix[x][y] = c

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

answer = 1e9
for i in range(1, V+1):
    answer = min(answer, matrix[i][i])

if answer == 1e9:
    print(-1)
else:
    print(answer)
