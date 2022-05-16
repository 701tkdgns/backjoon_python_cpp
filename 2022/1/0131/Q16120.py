S = input()
if S == 'P' or S == 'PPAP':
    print('PPAP')
else:
    stk = []
    pap = ['P', 'P', 'A', 'P']
    for i in S:
        stk.append(i)
        if stk[-4:] == pap:
            stk.pop()
            stk.pop()
            stk.pop()
    if ''.join(stk) == 'P' or ''.join(stk) == 'PPAP':
        print('PPAP')
    else:
        print('NP')

# s = input()
# if s == 'P' or s == 'PPAP':
#     print('PPAP')
# else:
#     stk = []
#     PPAP = ['P', 'P', 'A', 'P']
#     for i in s:
#         stk.append(i)
#         if stk[-4:] == PPAP:
#             stk.pop()
#             stk.pop()
#             stk.pop()
#     if stk == 'PPAP' or stk == ['P']:
#         print('PPAP')
#     else:
#         print('NP')

# s = input()
# if s == 'P' or s == 'PPAP':
#     print('PPAP')
# else:
#     stk = []
#     ppap = ['P', 'P', 'A', 'P']
#     for i in s:
#         stk.append(i)
#         if stk[-4:] == ppap:
#             stk.pop()
#             stk.pop()
#             stk.pop()
#     if stk == ppap or stk == ['P']:
#         print('PPAP')
#     else:
#         print('NP')
