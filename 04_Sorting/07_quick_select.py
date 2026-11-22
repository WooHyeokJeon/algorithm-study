# 1. 선택 (A[p...r]에서 i번째로 작은 원소를 찾음)
def select(arr, p, r, i):
    if p == r:
        return arr[p]
    q = partition(arr, p, r)
    k = q - p + 1
    if i < k:
        return select(arr, p, q - 1, i)
    elif i == k:
        return arr[q]
    else:
        return select(arr, q + 1, r, i - k)

# 2. 분할 (퀵 정렬과 동일)
def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] < x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

# 3. 테스트 (i는 1부터 시작)
A = [31, 8, 48, 73, 11, 3, 20, 29, 65, 15]
print(select(A, 0, len(A) - 1, 1))   # 3
print(select(A, 0, len(A) - 1, 7))   # 31