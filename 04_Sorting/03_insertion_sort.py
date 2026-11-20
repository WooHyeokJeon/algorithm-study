# 1. 삽입 정렬
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        newitem = arr[i]
        j = i - 1
        while j >= 0 and newitem < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = newitem
    return arr

# 2. 테스트
A = [3, 40, 32, 38, 8, 11, 50, 39, 65, 15]
print(insertion_sort(A))   # [3, 8, 11, 15, 32, 38, 39, 40, 50, 65]

B = [5, 2, 4, 3]
print(insertion_sort(B))   # [2, 3, 4, 5]