# S = input()
# T = input()
# s, t = len(S), len(T)
# lst = [[0 for _ in range(t + 1)] for _ in range(s + 1)]
# mx = 0
# for i in range(1, s + 1):
#     for j in range(1, t + 1):
#         if S[i - 1] == T[j - 1]:
#             lst[i][j] = lst[i - 1][j - 1] + 1
#         mx = max(mx, lst[i][j])
# print(mx)


S, T = input(), input()
s, t = len(S), len(T)
lst = [[0 for _ in range(t + 1)] for _ in range(s + 1)]
mx = 0
for i in range(1, s + 1):
    for j in range(1, t + 1):
        if S[i-1] == T[j-1]:
            lst[i][j] = lst[i - 1][j - 1] + 1
        mx = max(mx, lst[i][j])
print(mx)