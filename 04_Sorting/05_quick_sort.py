# 1. 퀵 정렬
def quick_sort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)
    return arr

# 2. 분할 (기준 원소 A[r]을 제자리에 놓고 그 위치를 리턴)
def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] < x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

# 3. 테스트
A = [31, 8, 48, 73, 11, 3, 20, 29, 65, 15]
print(quick_sort(A, 0, len(A) - 1))   # [3, 8, 11, 15, 20, 29, 31, 48, 65, 73]

B = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print(quick_sort(B, 0, len(B) - 1))   # [1, 2, 3, 4, 5, 6, 7, 8, 9]