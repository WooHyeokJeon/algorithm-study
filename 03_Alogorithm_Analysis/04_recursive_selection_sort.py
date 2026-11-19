# 1. 재귀 선택 정렬
# recursive_selection_sort() - 남은 원소 중 가장 큰 값을 맨 뒤로 보내고, 앞의 n-1개를 재귀로 정렬
def recursive_selection_sort(arr, n):
    # 기저 조건: 원소가 1개 이하이면 이미 정렬된 상태
    if n <= 1:
        return

    # arr[0..n-1]에서 최대값의 인덱스 찾기
    max_idx = 0
    for i in range(1, n):
        if arr[i] > arr[max_idx]:
            max_idx = i

    # 최대값을 맨 뒤(n-1)와 교환
    arr[n - 1], arr[max_idx] = arr[max_idx], arr[n - 1]

    # 앞의 n-1개를 같은 방식으로 정렬
    recursive_selection_sort(arr, n - 1)

# 2. 테스트
A = [5, 1, 6, 4, 2, 3]
recursive_selection_sort(A, len(A))
print(A)   # [1, 2, 3, 4, 5, 6]