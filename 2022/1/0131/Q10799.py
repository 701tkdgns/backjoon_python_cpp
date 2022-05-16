T = input()
stk = []
res = 0
for i in range(len(T)):
    if T[i] == '(':
        stk.append(T[i])
    else:
        if T[i - 1] == '(':
            stk.pop()
            res += len(stk)
        else:
            stk.pop()
            res += 1
print(res)





# # S = input()
# # stk, cnt = [], 0
# # for i in range(len(S)):
# #     if S[i] == '(':
# #         stk.append(S[i])
# #     else:
# #         if S[i-1] == '(':
# #             stk.pop()
# #             cnt += len(stk)
# #         else:
# #             stk.pop()
# #             cnt += 1
# #     print(cnt, stk)
