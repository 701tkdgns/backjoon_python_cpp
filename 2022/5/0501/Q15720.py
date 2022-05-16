B, C, D = map(int, input().split())  # ea
B_price = list(map(int, input().split()))
C_price = list(map(int, input().split()))
D_price = list(map(int, input().split()))

B_price.sort(reverse=True)
C_price.sort(reverse=True)
D_price.sort(reverse=True)

beforePrice, afterPrice = 0, 0

L = min(D, min(B, C))

for i in range(L):
    tmp = B_price[i] + C_price[i] + D_price[i]
    beforePrice += tmp
    afterPrice += tmp * 9 // 10
    B_price[i], C_price[i], D_price[i] = 0, 0, 0

tmp = sum(B_price) + sum(C_price) + sum(D_price)
beforePrice += tmp
afterPrice += tmp
print(beforePrice)
print(afterPrice)