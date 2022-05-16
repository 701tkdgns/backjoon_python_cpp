# for _ in range(int(input())):
#     N = int(input())
#     lst = [0 for _ in range(N+1)]
#     for _ in range(N):
#         t, i = map(int, input().split())
#         lst[t] = i
#
#     maxScore = lst[1]
#     cnt = 0
#     for i in range(1, N+1):
#         if lst[i] <= maxScore:
#             cnt += 1
#             maxScore = lst[i]
#     print(cnt)
#
# # s = 'ABCDE'
# #
# # for i in range(len(s)):
# #     for j in range(i, len(s)):
# #         for k in range(i, j + 1):
# #             print(s[k], end='')
# #         print()


for _ in range(int(input())):
    N = int(input())
    lst = [0 for _ in range(N+1)]
    for _ in range(N):
        t, i = map(int, input().split())
        lst[t] = i
    mx = lst[1]
    cnt = 0
    for i in range(1, N+1):
        if lst[i] <= mx:
            cnt += 1
            mx = lst[i]
    print(cnt)