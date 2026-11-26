# 1. 경로찾기 (Dynamic Programming)
def matrix_path(m):
    n = len(m)
    c = [[0] * n for _ in range(n)]

    # 1-1. 시작점과 첫 열, 첫 행
    c[0][0] = m[0][0]

    for i in range(1, n):
        c[i][0] = m[i][0] + c[i-1][0]

    for j in range(1, n):
        c[0][j] = m[0][j] + c[0][j-1]

    # 1-2. 나머지 칸은 위쪽과 왼쪽 중 작은 값을 더함
    for i in range(1, n):
        for j in range(1, n):
            c[i][j] = m[i][j] + min(c[i-1][j], c[i][j-1])

    return c[n-1][n-1]


# 2. 테스트
if __name__ == "__main__":
    m = [
        [6, 7, 12, 5],
        [5, 3, 11, 18],
        [7, 17, 3, 3],
        [8, 10, 14, 9]
    ]

    print(matrix_path(m))   # 40