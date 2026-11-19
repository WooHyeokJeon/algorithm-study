# 1. 퀵 정렬 호출 횟수 확인
# call_count - quick_sort()가 호출될 때마다 1씩 증가
call_count = 0

# quick_sort() - pivot 기준으로 left, middle, right로 나눈 뒤 재귀 정렬
def quick_sort(arr):
    global call_count
    call_count += 1

    # 기저 조건: 원소가 1개 이하이면 바로 반환
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # 나눈 left, right를 각각 재귀로 정렬
    return quick_sort(left) + middle + quick_sort(right)

# 2. 테스트
# 배열 크기에 따라 호출 횟수가 어떻게 변하는지 확인
A = [9, 8, 6, 12, 5, 7, 4, 10, 1, 14, 17, 20, 3, 11, 15]

call_count = 0
result = quick_sort(A)
print(result)        # [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 17, 20]
print(call_count)    # 호출 횟수 (피벗 선택에 따라 달라짐)

# 정렬된 배열을 넣으면 최악의 경우에 가까워짐
B = [1, 2, 3, 4, 5, 6, 7, 8]

call_count = 0
quick_sort(B)
print(call_count)    # 최악에 가까운 호출 횟수