import time
import random

# 1. 정렬 알고리즘 정의
# bubble_sort() - 인접한 두 원소를 비교해서 큰 값을 뒤로 보냄, O(n²)
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# insertion_sort() - 각 원소를 앞부분의 알맞은 위치에 끼워 넣음, O(n²)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

# quick_sort() - 피벗 기준으로 나눠서 재귀 정렬, 평균 O(n log n), 최악 O(n²)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# 2. 실행 시간 측정 함수
# measure() - 정렬 함수를 실행하고 걸린 시간을 초 단위로 반환
def measure(sort_func, data):
    start = time.time()
    sort_func(data[:])        # 원본이 바뀌지 않도록 복사본 사용
    return time.time() - start

# 3. 입력 크기별 비교
# 크기를 늘려 가며 세 정렬의 실행 시간을 비교
sizes = [500, 1000, 2000, 4000]

for n in sizes:
    data = [random.randint(1, 10000) for _ in range(n)]

    t_bubble = measure(bubble_sort, data)
    t_insertion = measure(insertion_sort, data)
    t_quick = measure(quick_sort, data)

    print(f"n = {n}")
    print(f"  Bubble Sort    : {t_bubble:.4f}초")
    print(f"  Insertion Sort : {t_insertion:.4f}초")
    print(f"  Quick Sort     : {t_quick:.4f}초")
    print()