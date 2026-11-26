# 1. 행렬 곱셈
def matrix_multiply(a, b):
    res = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += a[i][k] * b[k][j]

    return res


# 2. 행렬 거듭제곱 (분할정복)
def matrix_power(a, n):
    if n > 1:
        a = matrix_power(a, n // 2)
        a = matrix_multiply(a, a)

        if n % 2 == 1:
            b = [[1, 1], [1, 0]]
            a = matrix_multiply(a, b)

    return a


# 3. 피보나치 수
def fibonacci(n):
    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    x = [[1, 1], [1, 0]]
    y = matrix_power(x, n - 1)

    return y[0][0]


# 4. 테스트
if __name__ == "__main__":
    print(fibonacci(10))   # 55
    print(fibonacci(50))   # 12586269025