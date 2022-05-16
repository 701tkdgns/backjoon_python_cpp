# N = int(input())
# S = []
# for _ in range(N):
#     S.append(input())
# L = input()
# chk = [False for _ in range(N)]
# while True:
#     tmp = chk.copy()
#     for i, val in enumerate(S):
#         if val in L:
#             L = L.replace(val+' ', '')
#             tmp[i] = True
#     if chk == tmp:
#         break
#     else:
#         chk = tmp.copy()
#
# for i in S:
#     if i in L:
#         L = L.replace(i, '')
# if L == '':
#     print('Possible')
# else:
#     print('Impossible')


bird = []
N = int(input())
for _ in range(N):
    bird.append(list(map(str, input().split())))
question = list(map(str, input().split()))
check = False
for item in question:
    check = False
    for idx in range(N):
        if bird[idx]:
            if item == bird[idx][0]:
                del bird[idx][0]
                check = True
                break
    if not check:
        break
L = 0
for line in bird:
    L += len(line)
if check and L == 0:
    print("Possible")
else:
    print("Impossible")
