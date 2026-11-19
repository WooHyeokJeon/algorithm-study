# 1. 삼각형 합 계산 함수
# function5() - 이중 for문으로 A[i] * A[j]를 i < j인 쌍에 대해서만 더함
def function5(A, n):
    total = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            total += A[i] * A[j]

    return total

# 2. 반복 횟수 확인
# 바깥 루프가 i = 0일 때 안쪽은 n-1번, i = 1일 때 n-2번 ... 이런 식으로 줄어듦
# 전체 횟수는 (n-1) + (n-2) + ... + 1 = n(n-1)/2
def count_loop(n):
    count = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            count += 1

    return count

# 3. 테스트
A = [1, 2, 3, 4, 5]
n = len(A)

print(function5(A, n))     # 85
print(count_loop(n))       # 10 (= 5 * 4 / 2)
print(count_loop(10))      # 45 (= 10 * 9 / 2)