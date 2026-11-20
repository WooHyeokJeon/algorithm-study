# 1. 버블 정렬
def bubble_sort(arr):
    n = len(arr)
    for last in range(n - 1, 0, -1):
        for i in range(last):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

# 2. 버블 정렬 개선 (교환이 없으면 종료)
def bubble_sort2(arr):
    n = len(arr)
    for last in range(n - 1, 0, -1):
        sorted_flag = True
        for i in range(last):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted_flag = False
        if sorted_flag:
            return arr
    return arr

# 3. 테스트
A = [3, 31, 48, 73, 8, 11, 20, 29, 65, 15]
print(bubble_sort(A))   # [3, 8, 11, 15, 20, 29, 31, 48, 65, 73]

B = [3, 31, 48, 73, 8, 11, 20, 29, 65, 15]
print(bubble_sort2(B))   # [3, 8, 11, 15, 20, 29, 31, 48, 65, 73]

C = [1, 2, 3, 4, 5]
print(bubble_sort2(C))   # [1, 2, 3, 4, 5]