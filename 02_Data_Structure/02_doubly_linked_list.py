# 1. 노드 정의
# DListNode - 데이터(data)와 앞/뒤 노드를 가리키는 링크(llink, rlink)를 가짐
class DListNode:
    def __init__(self, data=None):
        self.data = data
        self.llink = None
        self.rlink = None

# 2. 이중 연결 리스트 정의
# head - 데이터가 없는 헤드 노드, 삽입/삭제 코드를 간단하게 해줌
class DoublyLinkedList:
    def __init__(self):
        self.head = DListNode()
        self.head.llink = self.head
        self.head.rlink = self.head

    # insert() - before 노드 바로 뒤에 새 노드를 삽입하고 새 노드를 반환
    def insert(self, before, data):
        newnode = DListNode(data)

        newnode.llink = before
        newnode.rlink = before.rlink
        before.rlink.llink = newnode
        before.rlink = newnode

        return newnode

    # delete() - removed 노드를 리스트에서 제거 (헤드 노드는 삭제하지 않음)
    def delete(self, removed):
        if removed == self.head:
            return

        removed.llink.rlink = removed.rlink
        removed.rlink.llink = removed.llink

    # print_list() - head 다음 노드부터 순서대로 데이터를 출력
    def print_list(self):
        p = self.head.rlink

        while p != self.head:
            print(p.data, end=" ")
            p = p.rlink

        print()

# 3. 테스트
L = DoublyLinkedList()

n1 = L.insert(L.head, 10)
n2 = L.insert(n1, 20)
n3 = L.insert(n2, 30)

L.print_list()   # 10 20 30
L.delete(n2)
L.print_list()   # 10 30