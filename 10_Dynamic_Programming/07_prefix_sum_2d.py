# 1. 2차원 누적합 만들기
def make_prefix(data):
    n = len(data)
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + data[i-1][j-1]

    return dp


# 2. 구간 합 구하기 ((x1, y1) ~ (x2, y2))
def range_sum(dp, x1, y1, x2, y2):
    return dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]


# 3. 테스트
if __name__ == "__main__":
    data = [
        [1, 4, 5, 10, 3],
        [2, 8, 9, 9, 5],
        [1, 3, 4, 9, 0],
        [2, 7, 6, 2, 0],
        [3, 4, 5, 8, 11]
    ]

    dp = make_prefix(data)

    print(range_sum(dp, 3, 2, 4, 4))   # 31
    print(range_sum(dp, 1, 1, 5, 5))   # 121