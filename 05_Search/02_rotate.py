import importlib

# 1. 01번 파일의 이진 검색 트리 가져오기
bst_file = importlib.import_module("01_binary_search_tree")


# 2. 회전 기능 추가
class RotateTree(bst_file.BinarySearchTree):
    # 3. 왼쪽 회전
    def rotate_left(self, tree):
        rightchild = tree.right
        tree.right = rightchild.left
        if rightchild.left is not None:
            rightchild.left.parent = tree
        rightchild.parent = tree.parent

        if tree.parent is None:
            self.root = rightchild
        elif tree == tree.parent.left:
            tree.parent.left = rightchild
        else:
            tree.parent.right = rightchild

        rightchild.left = tree
        tree.parent = rightchild

    # 4. 오른쪽 회전
    def rotate_right(self, tree):
        leftchild = tree.left
        tree.left = leftchild.right
        if leftchild.right is not None:
            leftchild.right.parent = tree
        leftchild.parent = tree.parent

        if tree.parent is None:
            self.root = leftchild
        elif tree == tree.parent.right:
            tree.parent.right = leftchild
        else:
            tree.parent.left = leftchild

        leftchild.right = tree
        tree.parent = leftchild


# 5. 테스트
if __name__ == "__main__":
    t = RotateTree()
    for x in [5, 3, 8, 6, 9]:
        t.insert(x)

    t.rotate_left(t.root)
    print(t.root.key)   # 8
    print(t.root.left.key)   # 5

    t.rotate_right(t.root)
    print(t.root.key)   # 5
    print(t.root.right.key)   # 8