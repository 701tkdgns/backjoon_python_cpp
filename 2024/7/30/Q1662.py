
def recursion(idx, v, length):
    if idx == len(S):
        return length

    if S[idx] == '(':
        stk.append([v, length - 1])
        length = 0
    elif S[idx] == ')':
        _v, _l = stk.pop()
        length = (int(_v) * length) + _l
    else:
        v = S[idx]
        length += 1


    return recursion(idx + 1, v, length)

S = input()
stk = []
res = recursion(0, '', 0)
print(res)

# 33(562(71(9)))

# def recursion(idx, v, length):
#     if idx == len(S):
#         return length
#     if S[idx] == '(':
#         stk.append([v, length - 1])
#         length = 0
#     elif S[idx] == ')':
#         _v, _l = stk.pop()
#         length = (int(_v) * length) + _l
#     else:
#         length += 1
#         v = S[idx]
#     return recursion(idx + 1, v, length)
#
#
# S = input()
# stk = []
# res = recursion(0, '', 0)
# print(res)