import heapq

# 1. 힙 생성과 삽입
# heappush() - 리스트를 최소 힙으로 유지하면서 값을 삽입, O(log n)
h = list()

heapq.heappush(h, 10)
heapq.heappush(h, 43)
heapq.heappush(h, 76)
heapq.heappush(h, 5)

print(h)               # [5, 10, 76, 43] (내부 배열 순서)

# 2. 최소값 확인
# h[0] - 루트가 항상 최소값이므로 바로 확인 가능, O(1)
print(h[0])            # 5

# 3. 최소값 삭제
# heappop() - 최소값을 꺼내고 힙 구조를 다시 맞춤, O(log n)
print(heapq.heappop(h))   # 5
print(heapq.heappop(h))   # 10
print(h)                  # [43, 76]

# 4. 리스트를 힙으로 만들기
# heapify() - 기존 리스트를 제자리에서 힙으로 변환, O(n)
data = [76, 10, 43, 5]
heapq.heapify(data)

print(data)            # [5, 10, 43, 76]
print(heapq.heappop(data))   # 5