# 1. 노드 클래스
class Node:
    def __init__(self):
        self.keys = []
        self.children = []
        self.parent = None


# 2. B-트리 클래스
class BTree:
    def __init__(self, k):
        self.k = k
        self.root = Node()

    # 3. 삽입할 리프 노드 찾기
    def find_leaf(self, x):
        r = self.root
        while r.children:
            i = 0
            while i < len(r.keys) and x > r.keys[i]:
                i += 1
            r = r.children[i]
        return r

    # 4. 삽입
    def insert(self, x):
        r = self.find_leaf(x)
        r.keys.append(x)
        r.keys.sort()
        if len(r.keys) > self.k:
            self.clear_overflow(r)

    # 5. 오버플로우 처리
    def clear_overflow(self, r):
        p = r.parent
        if p is not None:
            i = p.children.index(r)
            # 왼쪽 형제에게 넘기기
            if i > 0 and len(p.children[i - 1].keys) < self.k:
                left = p.children[i - 1]
                left.keys.append(p.keys[i - 1])
                p.keys[i - 1] = r.keys.pop(0)
                if r.children:
                    c = r.children.pop(0)
                    left.children.append(c)
                    c.parent = left
                return
            # 오른쪽 형제에게 넘기기
            if i < len(p.children) - 1 and len(p.children[i + 1].keys) < self.k:
                right = p.children[i + 1]
                right.keys.insert(0, p.keys[i])
                p.keys[i] = r.keys.pop()
                if r.children:
                    c = r.children.pop()
                    right.children.insert(0, c)
                    c.parent = right
                return

        # 둘로 분할하고 가운데 키를 부모로 올리기
        mid = len(r.keys) // 2
        up = r.keys[mid]
        new = Node()
        new.keys = r.keys[mid + 1:]
        r.keys = r.keys[:mid]
        if r.children:
            new.children = r.children[mid + 1:]
            r.children = r.children[:mid + 1]
            for c in new.children:
                c.parent = new

        if p is None:
            p = Node()
            p.children = [r]
            r.parent = p
            self.root = p

        i = p.children.index(r)
        p.keys.insert(i, up)
        p.children.insert(i + 1, new)
        new.parent = p
        if len(p.keys) > self.k:
            self.clear_overflow(p)


# 6. 테스트
if __name__ == "__main__":
    t = BTree(5)
    for x in [1, 2, 3, 4, 5, 6]:
        t.insert(x)

    print(t.root.keys)   # [4]
    print(t.root.children[0].keys)   # [1, 2, 3]
    print(t.root.children[1].keys)   # [5, 6]

    for x in [7, 8, 9, 10]:
        t.insert(x)

    print(t.root.keys)   # [5]
    print(t.root.children[0].keys)   # [1, 2, 3, 4]
    print(t.root.children[1].keys)   # [6, 7, 8, 9, 10]