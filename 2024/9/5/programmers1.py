def solution(m, n, b):
    answer: int = 0
    board: list = [list(row) for row in b]

    def checkBlock():
        remove_set = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != '' and board[i][j] == board[i][j + 1] and board[i][j] == board[i + 1][j] and board[i][
                    j] == board[i + 1][j + 1]:
                    remove_set.add((i, j))
                    remove_set.add((i + 1, j))
                    remove_set.add((i, j + 1))
                    remove_set.add((i + 1, j + 1))
        return remove_set

    def removeBlock(rs: set):
        for x, y in rs:
            board[x][y] = ''

    def fallDown():
        for j in range(n):
            land: int = m - 1
            for i in range(m - 1, -1, -1):
                if board[i][j] != '':
                    board[land][j] = board[i][j]
                    if land != i: board[i][j] = ''
                    land -= 1

    while True:
        remove_set: set = checkBlock()
        if len(remove_set) == 0: break
        answer += len(remove_set)
        removeBlock(remove_set)
        fallDown()
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/17679?language=python3