def preorder(i):
    if i == '.':
        return
    print(i, end='')
    preorder(tree[i][0])
    preorder(tree[i][1])


def inorder(i):
    if i == '.':
        return
    inorder(tree[i][0])
    print(i, end='')
    inorder(tree[i][1])


def postorder(i):
    if i == '.':
        return
    postorder(tree[i][0])
    postorder(tree[i][1])
    print(i, end='')


N = int(input())
tree = {}
for _ in range(N):
    I, L, R = input().split()
    tree[I] = [L, R]

preorder('A')
print()
inorder('A')
print()
postorder('A')