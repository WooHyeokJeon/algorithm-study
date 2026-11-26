# 1. LCS 길이 구하기
def lcs(x, y):
    m = len(x)
    n = len(y)

    dp = [[None] * (n+1) for _ in range(m+1)]

    # 1-1. 빈 문자열과의 LCS는 0
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]


# 2. 테스트
if __name__ == "__main__":
    print(lcs("GOOD MORNING.", "GUTEN MORGEN."))   # 7
    print(lcs("GOOGLES", "GOOSES"))   # 5