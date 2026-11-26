# 1. 피보나치 수 (재귀)
def fibonacci(n):
    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


# 2. 테스트
if __name__ == "__main__":
    print(fibonacci(10))   # 55
    print(fibonacci(14))   # 377