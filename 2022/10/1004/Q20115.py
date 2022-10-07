# N = int(input())
# drink = list(map(int, input().split()))
# drink.sort()
# while drink:
#     if len(drink) == 1:
#         break
#     a, b = drink[0], drink[-1]
#     del drink[0], drink[-1]
#     if a > b:
#         drink.append(a + (b / 2))
#     else:
#         drink.append(b + (a / 2))
#
# res = drink.pop()
# if res.is_integer():
#     print(int(res))
# else:
#     print(res)

N = int(input())
L = sorted(list(map(int, input().split())))
print(L.pop() + sum(L)/2)