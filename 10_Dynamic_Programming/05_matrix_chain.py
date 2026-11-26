# 1. 행렬 연쇄 곱셈 (Dynamic Programming)
def matrix_chain(p):
    n = len(p) - 1
    m = [[0] * (n+1) for _ in range(n+1)]

    # 1-1. 크기가 r인 구간을 작은 크기부터 채움
    for r in range(1, n):
        for i in range(1, n-r+1):
            j = i + r
            best = float("inf")

            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]

                if q < best:
                    best = q

            m[i][j] = best

    return m[1][n]


# 2. 테스트
if __name__ == "__main__":
    print(matrix_chain([10, 30, 5, 60]))   # 4500
    print(matrix_chain([4, 5, 9, 8, 10, 100, 5]))   # 5988