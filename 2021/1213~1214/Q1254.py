def pd(idx):
    tmp = 0
    for _ in range(idx+tmp, L-tmp-1):
        if S[idx+tmp] != S[L-tmp-1]:
            return False
    return True


S = input()
L, res = len(S), 0
for i in range(L):
    if pd(i):
        res = L + i
        break
print(res)










# def palindrome(idx):
#     tmp = 0
#     for i in range(idx+tmp, L-tmp-1):
#         if S[idx+tmp] != S[L-tmp-1]:
#             return False
#     return True
#
#
# S = input()
# L, res = len(S), 0
# for i in range(L):
#     if palindrome(i):
#         res = L + i
#         break
# print(res)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # # S = input()
# # # L = len(S)
# # # for i in range(L):
# # #     if S[i:] == S[i:][::-1]:
# # #         print(L+i)
# # #         break
# #
# # def palindrome(idx):
# #     tmp = 0
# #     for _ in range(idx+tmp, L-tmp-1):
# #         if S[idx+tmp] != S[L-tmp-1]:
# #             return False
# #         tmp += 1
# #     return True
# #
# #
# # S = input()
# # L, res = len(S), 0
# # for i in range(L):
# #     if palindrome(i):
# #         res = L + i
# #         break
# # print(res)
# # #
# # #
# # #
# # # # # S = input()
# # # #
# # # # lst = ['ABCD', 'BCD', 'PYTHON', 'JAVA', 'EFG', 'Z']
# # # #
# # # # # 문자열 길이 / 알파벳 사전순으로 정렬
# # # #
# # # # lst.sort(key=lambda x: (-len(x), x))
# # # #
# # # # print(lst)