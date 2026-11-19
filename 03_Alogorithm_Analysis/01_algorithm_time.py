# 1. 상수 시간 알고리즘 (O(1))
# function1() - 입력 크기 n과 상관없이 인덱스 하나만 접근
def function1(A, n):
    k = n // 2
    return A[k]

# 2. 선형 시간 알고리즘 (O(n))
# function2() - 배열의 모든 원소를 한 번씩 더함
def function2(A, n):
    total = 0

    for i in range(n):
        total += A[i]

    return total

# 3. 제곱 시간 알고리즘 (O(n²))
# function3() - 이중 for문으로 모든 쌍을 곱해서 더함
def function3(A, n):
    total = 0

    for i in range(n):
        for j in range(n):
            total += A[i] * A[j]

    return total

# 4. 테스트
# 입력 크기 n을 늘려도 function1은 한 번만 실행되고,
# function2는 n번, function3은 n²번 연산이 일어남
A = [1, 2, 3, 4, 5]
n = len(A)

print(function1(A, n))   # 3 (A[2])
print(function2(A, n))   # 15
print(function3(A, n))   # 225