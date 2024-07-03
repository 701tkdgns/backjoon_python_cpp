# import heapq
N = int(input())
room, hq = [], []
for _ in range(N):
    a, b = map(int, input().split())
    room.append([a, b])
room.sort(key=lambda x: (x[1], x[0]))
# heapq.heappush(hq, room[0][1])
res, end = 0, -1
# for idx in range(1, N):
#     if room[idx][0] < hq[0]:
#         heapq.heappush(hq, room[idx][1])
#     else:
#         heapq.heappop(hq)
#         heapq.heappush(hq, room[idx][1])
#     print(hq)
# print(len(hq))
for i in range(N):
    if end <= room[i][0]:
        end = room[i][1]
        res += 1
print(res)