# 1. 재귀 합 계산
# RecurrenceSum() - 배열의 첫 번째 원소를 더하고, 나머지 배열을 다시 재귀 호출
# 원소가 하나 남으면 그 값을 바로 반환 (기저 조건)
def RecurrenceSum(arr):
    if len(arr) == 1:
        return arr[0]

    return RecurrenceSum(arr[1:]) + arr[0]

# 2. 재귀 호출 횟수 확인
# 호출될 때마다 count를 늘려서 T(n) = T(n-1) + c 에서 c가 몇 번 쓰이는지 확인
count = 0

def RecurrenceSum_count(arr):
    global count
    count += 1

    if len(arr) == 1:
        return arr[0]

    return RecurrenceSum_count(arr[1:]) + arr[0]

# 3. 테스트
A = [1, 2, 3, 4, 5]

print(RecurrenceSum(A))          # 15

RecurrenceSum_count(A)
print(count)                     # 5 (배열 길이 n만큼 호출됨)