import importlib

# 1. 02번 파일의 회전 기능 가져오기
rotate_file = importlib.import_module("02_rotate")


# 2. 레드-블랙 트리 클래스
class RBTree(rotate_file.RotateTree):
    # 3. 노드 색깔 가져오기 (빈 노드는 검정)
    def get_color(self, node):
        if node is None:
            return 'B'
        return node.color

    # 4. 형제 노드 가져오기
    def get_sibling(self, node):
        if node == node.parent.left:
            return node.parent.right
        return node.parent.left

    # 5. 삽입 (노드는 빨강으로 삽입)
    def insert(self, x):
        super().insert(x)
        new_node = self.search(self.root, x)
        new_node.color = 'R'
        self.fix_tree(new_node)

    # 6. 삽입 후 색깔과 회전 맞추기
    def fix_tree(self, node):
        while node.parent is not None and node.parent.color == 'R':
            uncle = self.get_sibling(node.parent)
            # case 1
            if self.get_color(uncle) == 'R':
                node.parent.color = 'B'
                uncle.color = 'B'
                node.parent.parent.color = 'R'
                node = node.parent.parent
            else:
                if node.parent == node.parent.parent.left:
                    # case 2-1
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)
                    # case 2-2
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self.rotate_right(node.parent.parent)
                else:
                    # case 2-3
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)
                    # case 2-4
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self.rotate_left(node.parent.parent)
        self.root.color = 'B'


# 7. 테스트
if __name__ == "__main__":
    t = RBTree()
    for x in [99, 88, 62]:
        t.insert(x)

    print(t.root.key)   # 88
    print(t.root.color)   # B
    print(t.root.left.key)   # 62
    print(t.root.left.color)   # R
    print(t.root.right.key)   # 99
    print(t.root.right.color)   # R