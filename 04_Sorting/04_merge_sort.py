# 1. 병합 정렬
def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)
    return arr

# 2. 병합 (정렬된 두 부분을 tmp에 합친 뒤 arr에 복사)
def merge(arr, p, q, r):
    i = p
    j = q + 1
    t = 0
    tmp = [0] * (r - p + 1)
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp[t] = arr[i]
            i += 1
        else:
            tmp[t] = arr[j]
            j += 1
        t += 1
    while i <= q:
        tmp[t] = arr[i]
        i += 1
        t += 1
    while j <= r:
        tmp[t] = arr[j]
        j += 1
        t += 1
    for k in range(r - p + 1):
        arr[p + k] = tmp[k]

# 3. 테스트
A = [31, 3, 65, 73, 8, 11, 20, 29, 48, 15]
print(merge_sort(A, 0, len(A) - 1))   # [3, 8, 11, 15, 20, 29, 31, 48, 65, 73]

B = [5, 2, 4, 6, 1, 3]
print(merge_sort(B, 0, len(B) - 1))   # [1, 2, 3, 4, 5, 6]