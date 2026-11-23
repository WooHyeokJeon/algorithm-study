import importlib

# 1. 01번 파일의 B-트리 가져오기
insert_file = importlib.import_module("01_b_tree_insert")


# 2. 삭제 기능 추가
class BTreeDelete(insert_file.BTree):
    # 3. 키 x를 가진 노드 찾기
    def find_node(self, x):
        r = self.root
        while True:
            if x in r.keys:
                return r
            if not r.children:
                return None
            i = 0
            while i < len(r.keys) and x > r.keys[i]:
                i += 1
            r = r.children[i]

    # 4. 부모 p의 idx번째 자식과 idx + 1번째 자식 병합
    def merge(self, p, idx):
        left = p.children[idx]
        right = p.children[idx + 1]
        left.keys += [p.keys[idx]] + right.keys
        for c in right.children:
            c.parent = left
        left.children += right.children
        del p.keys[idx]
        del p.children[idx + 1]

    # 5. 삭제
    def delete(self, x):
        v = self.find_node(x)
        if v is None:
            return

        i = v.keys.index(x)
        if v.children:
            # 직후원소를 가진 리프 찾기
            r = v.children[i + 1]
            while r.children:
                r = r.children[0]
            v.keys[i] = r.keys.pop(0)
        else:
            r = v
            r.keys.pop(i)

        if len(r.keys) < self.k // 2:
            self.clear_underflow(r)

    # 6. 언더플로우 처리
    def clear_underflow(self, r):
        p = r.parent
        if p is None:
            if not r.keys and r.children:
                self.root = r.children[0]
                self.root.parent = None
            return

        i = p.children.index(r)
        # 왼쪽 형제에게 빌리기
        if i > 0 and len(p.children[i - 1].keys) > self.k // 2:
            left = p.children[i - 1]
            r.keys.insert(0, p.keys[i - 1])
            p.keys[i - 1] = left.keys.pop()
            if left.children:
                c = left.children.pop()
                r.children.insert(0, c)
                c.parent = r
            return
        # 오른쪽 형제에게 빌리기
        if i < len(p.children) - 1 and len(p.children[i + 1].keys) > self.k // 2:
            right = p.children[i + 1]
            r.keys.append(p.keys[i])
            p.keys[i] = right.keys.pop(0)
            if right.children:
                c = right.children.pop(0)
                r.children.append(c)
                c.parent = r
            return
        # 형제와 병합하기
        if i > 0:
            self.merge(p, i - 1)
        else:
            self.merge(p, i)
        if len(p.keys) < self.k // 2:
            self.clear_underflow(p)


# 7. 테스트
if __name__ == "__main__":
    t = BTreeDelete(5)
    for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        t.insert(x)

    t.delete(4)
    print(t.root.children[0].keys)   # [1, 2, 3]

    t.delete(1)
    print(t.root.children[0].keys)   # [2, 3]

    t.delete(2)
    print(t.root.keys)   # [6]
    print(t.root.children[0].keys)   # [3, 5]
    print(t.root.children[1].keys)   # [7, 8, 9, 10]

    t.delete(6)
    print(t.root.keys)   # [7]
    print(t.root.children[1].keys)   # [8, 9, 10]