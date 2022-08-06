













# import heapq
# N = int(input())
# times = [0] * (N + 1)
# graph = {}
# for i in range(1, N + 1):
#     tmp = list(map(int, input().split()))
#     times[i] = tmp[0]
#     if tmp[1] == 0:
#         continue
#     for j in tmp[2:]:
#         if i in graph:
#             graph[i].append(j)
#         else:
#             graph[i] = [j]