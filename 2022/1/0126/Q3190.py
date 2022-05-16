N = int(input())
board = [[0 for _ in range(N + 1)] * (N + 1)]
K = int(input())
apple, snake = [], []
for _ in range(K):
    a, b = map(int, input().split())
    apple.append((a, b))
    board[a][b] = 1
L = int(input())
for _ in range(L):
    a, b = map(int, input().split())
    snake.append((a, b))
