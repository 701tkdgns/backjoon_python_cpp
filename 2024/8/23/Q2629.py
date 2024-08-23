import sys
input = sys.stdin.readline


def dfs(idx: int, weight: int, _max: int, dp: list, weights: list):
    if idx > _max: return
    if dp[idx][weight] == 1: return
    dp[idx][weight] = 1
    dfs(idx + 1, abs(weight - weights[idx - 1]), _max, dp, weights)
    dfs(idx + 1, weight, _max, dp, weights)
    dfs(idx + 1, weight + weights[idx - 1], _max, dp, weights)


def main():
    N: int = int(input())
    weights: list = list(map(int, input().split()))
    m: int = int(input())
    balls: list = list(map(int, input().split()))
    dp: list = [[0 for _ in range(15001)] for _ in range(31)]
    dfs(0, 0, N, dp, weights)
    for i in range(m):
        if balls[i] > 15001:
            print('N', end=' ')
        elif dp[N][balls[i]] == 1:
            print('Y', end=' ')
        else:
            print('N', end=' ')


if __name__ == '__main__':
    main()
