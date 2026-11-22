# 1. 노드 클래스
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


# 2. 이진 검색 트리 클래스
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # 3. 검색
    def search(self, t, x):
        if t is None or t.key == x:
            return t
        if x < t.key:
            return self.search(t.left, x)
        return self.search(t.right, x)

    # 4. 삽입
    def insert(self, x):
        r = Node(x)
        if self.root is None:
            self.root = r
            return
        p = None
        tmp = self.root
        while tmp is not None:
            p = tmp
            if x < tmp.key:
                tmp = tmp.left
            else:
                tmp = tmp.right
        r.parent = p
        if x < p.key:
            p.left = r
        else:
            p.right = r


# 5. 테스트
if __name__ == "__main__":
    bst = BinarySearchTree()
    for x in [23, 11, 139, 1, 14, 67, 871]:
        bst.insert(x)
    bst.insert(55)

    print(bst.search(bst.root, 14).key)   # 14
    print(bst.search(bst.root, 55).key)   # 55
    print(bst.search(bst.root, 100))   # None