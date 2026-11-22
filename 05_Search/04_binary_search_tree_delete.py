import importlib

# 1. 01번 파일의 이진 검색 트리 가져오기
bst_file = importlib.import_module("01_binary_search_tree")


# 2. 삭제 기능 추가
class BinarySearchTreeDelete(bst_file.BinarySearchTree):
    # 3. 노드 u를 노드 v로 바꾸기
    def replace(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v is not None:
            v.parent = u.parent

    # 4. 삭제
    def delete(self, x):
        r = self.search(self.root, x)
        if r is None:
            return

        # case 1 자식이 0개 또는 1개
        if r.left is None:
            self.replace(r, r.right)
        elif r.right is None:
            self.replace(r, r.left)
        # case 3 자식이 2개
        else:
            s = r.right
            while s.left is not None:
                s = s.left

            if s.parent != r:
                self.replace(s, s.right)
                s.right = r.right
                s.right.parent = s

            self.replace(r, s)
            s.left = r.left
            s.left.parent = s


# 5. 테스트
if __name__ == "__main__":
    t = BinarySearchTreeDelete()
    for x in [23, 11, 139, 1, 14, 67]:
        t.insert(x)

    t.delete(14)
    print(t.search(t.root, 14))   # None

    t.delete(139)
    print(t.root.right.key)   # 67

    t.delete(23)
    print(t.root.key)   # 67
    print(t.root.left.key)   # 11