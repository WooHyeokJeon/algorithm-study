# 1. 최소 힙 정의
# MinHeap - 완전 이진 트리를 배열(list)로 저장, 부모 노드가 자식 노드보다 작거나 같음
class MinHeap:
    def __init__(self):
        self.heap = []

    # insert() - 제일 마지막 자리에 넣은 뒤, 부모와 비교하며 위로 올림
    def insert(self, item):
        self.heap.append(item)
        i = len(self.heap) - 1

        # 부모 인덱스는 (i - 1) // 2
        while i > 0 and self.heap[i] < self.heap[(i - 1) // 2]:
            parent = (i - 1) // 2
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent

    # delete_min() - 루트(최소값)를 꺼내고, 마지막 원소를 루트로 올린 뒤 자식과 비교하며 아래로 내림
    def delete_min(self):
        if not self.heap:
            print("Heap is empty")
            return None

        min_item = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._down(0)

        return min_item

    # _down() - 현재 위치의 값을 자식들과 비교해서 더 작은 자식과 자리를 바꾸며 내려감
    def _down(self, i):
        n = len(self.heap)

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            # 더 이상 바꿀 자식이 없으면 종료
            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

    # peek() - 삭제하지 않고 최소값만 확인
    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]

# 2. 테스트
# 파일을 직접 실행할 때만 동작하도록 감싸서, 다른 파일에서 import해도 출력되지 않음
if __name__ == "__main__":
    h = MinHeap()

    h.insert(2)
    h.insert(52)
    h.insert(8)
    h.insert(13)
    h.insert(37)
    h.insert(67)
    h.insert(161)

    print(h.heap)           # 힙 배열 상태 출력
    print(h.peek())         # 2

    # 슬라이드 32페이지: 7 삽입
    h.insert(7)
    print(h.heap)

    print(h.delete_min())   # 2
    print(h.delete_min())   # 7
    print(h.heap)