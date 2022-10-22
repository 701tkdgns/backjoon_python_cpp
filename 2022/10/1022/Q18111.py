import sys
res = sys.maxsize

N, M, B = map(int, input().split())
lst = []
height = 0
for _ in range(N):
    lst.append(list(map(int, input().split())))
# 0층부터 256층까지 반복
for t in range(257):
    _max, _min = 0, 0
    # 블록 확인
    for i in range(N):
        for j in range(M):
            # 블록이 층 수보다 더 크면
            if lst[i][j] >= t:
                _max += lst[i][j] - t
            # 블록이 층 수보다 더 작으면
            else:
                _min += t - lst[i][j]

    # 블록을 뺀 것과 원래 있던 블록의 합과 블록을 더한 값을 비교
    # 블록을 뺀 것과 원래 있던 블록의 합이 더 커야 층을 만들 수 있음.
    if _max + B - _min >= 0:
        if _min + (_max * 2) <= res:
            res = _min + (_max * 2)
            height = t
print(res, height)











# import sys
#
# N, M, B = map(int, input().split())
# lst = []
# res = sys.maxsize
# idx = 0
# # 출력 : 시간, 높이
# for _ in range(N):
#     lst.append(list(map(int, input().split())))
#
# for t in range(257):
#     _max, _min = 0, 0
#     for i in range(N):
#         for j in range(M):
#             if lst[i][j] >= t:
#                 _max += lst[i][j] - t   # 올려야 할 값
#             else:
#                 _min += t - lst[i][j]   # 내려야 할 값
#
#     if _max + B >= _min:
#         if _min + (_max * 2) <= res:
#             res = _min + (_max * 2)
#             idx = t
# print(res, idx)
