import importlib

# 1. 힙 모듈 불러오기
# 09_heap.py는 숫자로 시작해서 일반 import가 안 되므로 importlib로 불러옴
heap_module = importlib.import_module("09_heap")
MinHeap = heap_module.MinHeap

# 2. 우선순위 큐 정의
# PriorityQueue - 값이 작을수록 우선순위가 높다고 보고, 최소 힙으로 구현
class PriorityQueue:
    def __init__(self):
        self.heap = MinHeap()

    # enqueue() - 우선순위 값을 힙에 삽입, O(log n)
    def enqueue(self, item):
        self.heap.insert(item)

    # dequeue() - 가장 우선순위가 높은(가장 작은) 항목을 꺼내서 반환, O(log n)
    def dequeue(self):
        return self.heap.delete_min()

    # peek() - 가장 우선순위가 높은 항목을 꺼내지 않고 확인, O(1)
    def peek(self):
        return self.heap.peek()

    # is_empty() - 큐가 비어 있는지 확인
    def is_empty(self):
        return len(self.heap.heap) == 0

# 3. 테스트
pq = PriorityQueue()

pq.enqueue(20)
pq.enqueue(2)
pq.enqueue(17)
pq.enqueue(5)

print(pq.peek())       # 2
print(pq.dequeue())    # 2
print(pq.dequeue())    # 5
print(pq.dequeue())    # 17
print(pq.dequeue())    # 20
print(pq.is_empty())   # True