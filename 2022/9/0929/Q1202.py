import sys
import heapq
input = sys.stdin.readline
N, K = map(int, input().split())
jew = []
for _ in range(N):
    heapq.heappush(jew, list(map(int, input().split())))
bags = []
for _ in range(K):
    bags.append(int(input()))
bags.sort()
res = 0
tmp_jew = []
for bag in bags:
    while jew and bag >= jew[0][0]:
        heapq.heappush(tmp_jew, -heapq.heappop(jew)[1]) # 최대힙 정렬 : 최대값 먼저 출력
    if tmp_jew:
        res -= heapq.heappop(tmp_jew)
    elif not jew:
        break
print(res)

# N, k = map(int, input().split())
# lst = []
# for _ in range(N):
#     M, V = map(int, input().split())
#     lst.append([M, V])
# lst.sort()
# K, visit_K = [], [False for _ in range(k)]
# for _ in range(k):
#     K.append(int(input()))
# K.sort()
# res, idx = 0, 0
# while idx < k:
#     s, e = 0, len(lst)-1
#     _max, _max_idx = 0, 0
#     while s < e:
#         if s < len(lst) and lst[s][0] <= K[idx]:
#             if not visit_K[s] and _max < lst[s][1]:
#                 _max = lst[s][1]
#                 _max_idx = s
#             s += 1
#         elif e < len(lst) and lst[e][0] <= K[idx]:
#             if not visit_K[e] and _max < lst[e][1]:
#                 _max = lst[e][1]
#                 _max_idx = e
#             e -= 1
#         else:
#             s += 1
#             e -= 1
#     res += _max
#     visit_K[_max_idx] = True
#     idx += 1
# print(res)