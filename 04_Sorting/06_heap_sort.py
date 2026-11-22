# 1. 내려가기 (arr[k]를 루트로 하는 서브 트리를 최대 힙으로)
def percolate_down(arr, k, n):
    child = 2 * k + 1
    right = 2 * k + 2
    if child <= n - 1:
        if right <= n - 1 and arr[child] < arr[right]:
            child = right
        if arr[k] < arr[child]:
            arr[k], arr[child] = arr[child], arr[k]
            percolate_down(arr, child, n)

# 2. 힙 구성
def build_heap(arr, n):
    for i in range((n - 2) // 2, -1, -1):
        percolate_down(arr, i, n)

# 3. 최댓값 삭제 (힙 크기를 1 줄임)
def delete_max(arr, n):
    mx = arr[0]
    arr[0] = arr[n - 1]
    percolate_down(arr, 0, n - 1)
    return mx

# 4. 힙 정렬
def heap_sort(arr):
    n = len(arr)
    build_heap(arr, n)
    for i in range(n - 1, 0, -1):
        arr[i] = delete_max(arr, i + 1)
    return arr

# 5. 테스트
A = [4, 2, 8, 7, 3, 3, 5, 1, 9]
print(heap_sort(A))   # [1, 2, 3, 3, 4, 5, 7, 8, 9]

B = [5, 4, 3, 2, 1]
print(heap_sort(B))   # [1, 2, 3, 4, 5]