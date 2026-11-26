# 1. 피보나치 수 (Memoization)
def fibonacci(n, memo):
    if n <= 1:
        return n

    if memo[n] != -1:
        return memo[n]

    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)

    return memo[n]


# 2. 테스트
if __name__ == "__main__":
    memo = [0, 1] + [-1] * 100

    print(fibonacci(6, memo))   # 8
    print(fibonacci(50, memo))   # 12586269025