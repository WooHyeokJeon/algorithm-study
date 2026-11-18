# 1. 원형 큐 설정
# MAX_QUEUE_SIZE - 배열의 크기, 한 칸은 항상 비워 두므로 저장 가능한 개수는 MAX_QUEUE_SIZE - 1
MAX_QUEUE_SIZE = 8

class CircularQueue:
    def __init__(self):
        self.data = [None] * MAX_QUEUE_SIZE
        self.front = 0
        self.rear = 0

    # is_empty() - front와 rear가 같으면 빈 큐
    def is_empty(self):
        return self.front == self.rear

    # is_full() - rear 다음 칸이 front와 같으면 가득 찬 큐
    def is_full(self):
        return (self.rear + 1) % MAX_QUEUE_SIZE == self.front

    # enqueue() - rear를 한 칸 옮긴 뒤 그 위치에 데이터를 저장
    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return

        self.rear = (self.rear + 1) % MAX_QUEUE_SIZE
        self.data[self.rear] = item

    # dequeue() - front를 한 칸 옮긴 뒤 그 위치의 데이터를 꺼내서 반환
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        self.front = (self.front + 1) % MAX_QUEUE_SIZE
        return self.data[self.front]

    # print_queue() - front 다음 칸부터 rear까지 순서대로 출력
    def print_queue(self):
        i = self.front

        while i != self.rear:
            i = (i + 1) % MAX_QUEUE_SIZE
            print(self.data[i], end=" ")

        print()

# 2. 테스트
q = CircularQueue()

q.enqueue('A')
q.enqueue('B')
q.print_queue()          # A B
print(q.dequeue())       # A

q.enqueue('C')
q.enqueue('D')
q.print_queue()          # B C D

# 가득 찬 상태 테스트
# 현재 3개가 들어 있고 최대 7개까지 저장 가능하므로 5번째 이후 추가부터 Queue is full 출력
for i in range(5):
    q.enqueue(i)
q.print_queue()