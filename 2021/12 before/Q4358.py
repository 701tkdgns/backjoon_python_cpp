tree = dict()
cnt = 0
while True:
    try:
        S = input()
        tree[S] = tree.get(S, 0) + 1
        cnt += 1
    except EOFError:
        break

lst = sorted(tree.items(), key=lambda x: x[0])

for key, value in lst:
    print('{} {:.4f}'.format(key, (value/cnt)*100))
