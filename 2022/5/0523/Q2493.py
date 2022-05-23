N = int(input())
lst = list(map(int, input().split()))
stk = []
res = [0 for _ in range(N)]
for i in range(N):
    while stk:
        if stk[-1][1] > lst[i]:
            res[i] = stk[-1][0] + 1
            break
        else:
            stk.pop()
    stk.append([i, lst[i]])
print(*res)
































# N = int(input())
# lst = list(map(int, input().split()))
# stk = []
# res = [0 for _ in range(N)]
# for i in range(N):
#     while stk:
#         if stk[-1][1] > lst[i]:
#             res[i] = stk[-1][0] + 1
#             break
#         else:
#             stk.pop()
#     stk.append([i, lst[i]])
# print(*res)
