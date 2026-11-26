# 1. 피보나치 수 (Tabulation)
def fibonacci(n):
    if n <= 1:
        return n

    ft = [0] * (n + 1)
    ft[1] = 1

    for i in range(2, n + 1):
        ft[i] = ft[i-1] + ft[i-2]

    return ft[n]


# 2. 테스트
if __name__ == "__main__":
    print(fibonacci(10))   # 55
    print(fibonacci(50))   # 12586269025