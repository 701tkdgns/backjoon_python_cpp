def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board]

    def check():
        to_remove = set()
        for i in range(m - 1):
            for j in range(n - 1):
                # 현재 위치와 우측, 하단, 대각선 위치의 블록이 모두 동일한지 확인
                if board[i][j] != '' and board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                    to_remove.add((i, j))
                    to_remove.add((i + 1, j))
                    to_remove.add((i, j + 1))
                    to_remove.add((i + 1, j + 1))
        return to_remove

    def remove_blocks(to_remove):
        for i, j in to_remove:
            board[i][j] = ''

    def drop_blocks():
        for j in range(n):
            empty_row = m - 1
            for i in range(m - 1, -1, -1):
                if board[i][j] != '':
                    board[empty_row][j] = board[i][j]
                    if empty_row != i:
                        board[i][j] = ''
                    empty_row -= 1

    while True:
        to_remove = check()
        if not to_remove:
            break
        answer += len(to_remove)
        remove_blocks(to_remove)
        drop_blocks()

    return answer