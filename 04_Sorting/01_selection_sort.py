# 1. 선택 정렬
def selection_sort(arr):
    n = len(arr)
    for last in range(n - 1, 0, -1):
        k = 0
        for i in range(1, last + 1):
            if arr[i] > arr[k]:
                k = i
        arr[k], arr[last] = arr[last], arr[k]
    return arr

# 2. 테스트
A = [8, 31, 48, 73, 3, 65, 20, 29, 11, 15]
print(selection_sort(A))   # [3, 8, 11, 15, 20, 29, 31, 48, 65, 73]

B = [5, 1, 6, 4, 2, 3]
print(selection_sort(B))   # [1, 2, 3, 4, 5, 6]