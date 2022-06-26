# S = input()
# stk = []
# length = 0
# tmp = ''
# for c in S:
#     if c.isdigit():
#         length += 1
#         tmp = c
#     elif c == '(':
#         stk.append((tmp, length-1))
#         length = 0
#     else:
#         multi, preL = stk.pop()
#         length = (int(multi) * length) + preL
#
# print(length)

def recursion(idx, tmp, length):
    if idx == len(S):
        return length
    if S[idx].isdigit():
        length += 1
        tmp = S[idx]
    elif S[idx] == '(':
        stk.append((tmp, length - 1))
        length = 0
    else:
        multi, preL = stk.pop()
        length = (int(multi) * length) + preL
    return recursion(idx+1, tmp, length)


S = input()
stk = []
res = recursion(0, '', 0)
print(res)
