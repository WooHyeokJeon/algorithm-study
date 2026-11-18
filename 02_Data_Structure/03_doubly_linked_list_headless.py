# 1. 노드 정의
# Node - 데이터(data)와 앞/뒤 노드를 가리키는 링크(prev, next)를 가짐
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# 2. 헤드 노드 없이 이중 연결 리스트 정의
# head - 첫 번째 노드, tail - 마지막 노드, 비어 있으면 둘 다 None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # insert_first() - 리스트 맨 앞에 새 노드를 삽입
    def insert_first(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

    # insert_last() - 리스트 맨 뒤에 새 노드를 삽입
    def insert_last(self, data):
        new = Node(data)

        if self.tail is None:
            self.head = new
            self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new

    # insert_after() - target 값을 가진 첫 번째 노드 바로 뒤에 새 노드를 삽입
    def insert_after(self, target, data):
        node = self.search(target)

        if node is None:
            return

        new = Node(data)
        new.prev = node
        new.next = node.next

        if node.next is not None:
            node.next.prev = new
        else:
            self.tail = new

        node.next = new

    # delete_first() - 첫 번째 노드를 삭제
    def delete_first(self):
        if self.head is None:
            return

        if self.head is self.tail:
            self.head = None
            self.tail = None
            return

        self.head = self.head.next
        self.head.prev = None

    # delete_last() - 마지막 노드를 삭제
    def delete_last(self):
        if self.tail is None:
            return

        if self.head is self.tail:
            self.head = None
            self.tail = None
            return

        self.tail = self.tail.prev
        self.tail.next = None

    # delete() - data 값을 가진 첫 번째 노드를 삭제, 없으면 아무 작업도 하지 않음
    def delete(self, data):
        node = self.search(data)

        if node is None:
            return

        if node is self.head:
            self.delete_first()
            return

        if node is self.tail:
            self.delete_last()
            return

        node.prev.next = node.next
        node.next.prev = node.prev

    # search() - data 값을 가진 첫 번째 노드를 찾아 반환, 없으면 None 반환
    def search(self, data):
        cur = self.head

        while cur is not None:
            if cur.data == data:
                return cur
            cur = cur.next

        return None

    # print_forward() - head부터 tail 방향으로 데이터를 출력
    def print_forward(self):
        cur = self.head

        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next

        print()

    # print_backward() - tail부터 head 방향으로 데이터를 출력
    def print_backward(self):
        cur = self.tail

        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.prev

        print()

# 3. 테스트
L = DoublyLinkedList()

# 삽입 테스트
L.insert_first(20)
L.insert_first(10)
L.insert_last(30)
L.insert_last(40)

print("Forward:")
L.print_forward()    # 10 20 30 40
print("Backward:")
L.print_backward()   # 40 30 20 10

# 중간 삽입 테스트
L.insert_after(20, 25)
print("After insert:")
L.print_forward()    # 10 20 25 30 40

# 삭제 테스트
L.delete_first()
L.delete_last()
L.delete(25)
print("After delete:")
L.print_forward()    # 20 30

# 탐색 테스트
node = L.search(30)

if node is not None:
    print("Found:", node.data)   # Found: 30
else:
    print("Not found")