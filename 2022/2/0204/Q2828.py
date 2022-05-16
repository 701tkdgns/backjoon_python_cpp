N, M = map(int, input().split())
J = int(input())
res = 0
idx = 1
for i in range(J):
    val = int(input())
    if val < idx:
        res += idx - val
        idx = val
    elif val > idx + M - 1:
        res += val - (idx + M - 1)
        idx = val - M + 1
print(res)

# N, M = map(int, input().split())
# J = int(input())
# res, idx = 0, 1
# # 바구니 위치 : 왼쪽 + 바구니 크기 - 1
# for i in range(J):
#     val = int(input())
#     if val < idx:   # 사과가 바구니의 왼쪽보다 이전 위치에 떨어질 경우 : 왼쪽 - 사과
#         res += idx - val
#         idx = val
#     elif val > idx + M - 1:     # 사과가 바구니의 오른쪽 너머에서 떨어질 경우 : 사과 - 오른쪽
#         res += val - (idx + M - 1)
#         idx = val - M + 1
#     else:
#         pass    # 바구니의 왼쪽 ~ 오른쪽 사이에 사과 떨이질 경우
# print(res)