# 1. LCS 문자열 구하기
def lcs_string(x, y):
    m = len(x)
    n = len(y)

    # 1-1. dp 테이블 만들기
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # 1-2. 오른쪽 아래에서 거슬러 올라가며 문자 수집
    res = []
    i = m
    j = n

    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            res.append(x[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(res))


# 2. 테스트
if __name__ == "__main__":
    print(lcs_string("GOOD MORNING.", "GUTEN MORGEN."))   # G MORG.
    print(lcs_string("GOOGLES", "GOOSES"))   # GOOES