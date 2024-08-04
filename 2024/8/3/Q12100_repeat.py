from copy import deepcopy


def move(idx, board, n):
    if idx == 0:
        for i in range(n):
            top = n - 1
            for j in range(n - 2, -1, -1):
                if board[i][j] != 0:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = tmp
                    elif board[i][top] == tmp:
                        board[i][top] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        board[i][top] = tmp
    elif idx == 1:
        for i in range(n):
            top = 0
            for j in range(1, n):
                if board[i][j] != 0:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = tmp
                    elif board[i][top] == tmp:
                        board[i][top] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        board[i][top] = tmp
    elif idx == 2:
        for j in range(n):
            top = n - 1
            for i in range(n - 2, -1, -1):
                if board[i][j] != 0:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = tmp
                    elif board[top][j] == tmp:
                        board[top][j] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        board[top][j] = tmp
    elif idx == 3:
        for j in range(n):
            top = 0
            for i in range(1, n):
                if board[i][j] != 0:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = tmp
                    elif board[top][j] == tmp:
                        board[top][j] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        board[top][j] = tmp

    return board


def dfs(level, board, res, n):
    if level == 5:
        for i in range(n):
            for j in range(n):
                res = max(res, board[i][j])
        return res

    for i in range(4):
        moved_board = move(i, deepcopy(board), n)
        res = max(res, dfs(level + 1, moved_board, res, n))
    return res


def main():
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    res = dfs(0, graph, 0, N)
    print(res)


if __name__ == "__main__":
    main()