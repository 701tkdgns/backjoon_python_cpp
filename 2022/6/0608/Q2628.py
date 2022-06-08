w, h = map(int, input().split())
x, y = [0, w], [0, h]
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == 0:
        x.append(b)
    else:
        y.append(b)
x.sort()
y.sort()
res = 0
W, H = [], []
for i in range(len(x)-1):
    W.append(x[i+1]-x[i])
for i in range(len(y)-1):
    H.append(y[i+1]-y[i])
print(max(W)*max(H))
