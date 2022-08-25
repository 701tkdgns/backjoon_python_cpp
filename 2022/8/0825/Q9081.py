T = int(input())
for _ in range(T):
    arr = list(input())
    flag = False
    for i in range(1, len(arr)):
        if arr[-i] > arr[-i-1]:
            tmp = i
            flag = True
            break
    if flag == False:
        print("".join(arr))
        continue
    minimum = max(arr)
    for j in range(tmp-1, len(arr)):
        if arr[j] > arr[-tmp-1]:
            minimum = min(minimum, arr[j])
            minum = j
    arr[-tmp-1], arr[minum] = arr[minum], arr[-tmp-1]
    tmpsort = sorted(arr[-tmp:])
    result = arr[0:-tmp]+tmpsort
    print("".join(result))

# import sys, heapq
# sys.setrecursionlimit(10 ** 6)
#
#
# def backtrack(v):
#     if len(v) == len(S):
#         if v not in lst:
#             heapq.heappush(lst, v)
#         return
#
#     for i in range(len(S)):
#         if not visit[i]:
#             visit[i] = True
#             backtrack(v + S[i])
#             visit[i] = False
#
#
# for _ in range(int(input())):
#     S = input()
#     lst = []
#     visit = [False for _ in range(len(S))]
#     backtrack('')
#     while lst:
#         tmp = heapq.heappop(lst)
#         if lst and tmp == S:
#             print(heapq.heappop(lst))
#             break
#     if not lst:
#         print(S)
