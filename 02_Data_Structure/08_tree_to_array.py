# 1. 노드 정의
# TreeNode - 값(key)과 왼쪽/오른쪽 자식 노드를 가짐
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# 2. 트리를 배열로 변환
# tree_to_array() - 루트를 0번 인덱스에 두고, 왼쪽 자식은 2k + 1, 오른쪽 자식은 2k + 2 위치에 저장
def tree_to_array(root):
    if root is None:
        return []

    array = []
    queue = [(root, 0)]

    while queue:
        node, index = queue.pop(0)

        # 해당 인덱스까지 배열을 None으로 늘려서 자리를 확보
        if index >= len(array):
            array.extend([None] * (index - len(array) + 1))

        array[index] = node.key

        if node.left:
            queue.append((node.left, 2 * index + 1))
        if node.right:
            queue.append((node.right, 2 * index + 2))

    return array

# 3. 테스트
# 슬라이드 18페이지의 완전 이진 트리
root = TreeNode(2)
root.left = TreeNode(7)
root.right = TreeNode(52)
root.left.left = TreeNode(13)
root.left.right = TreeNode(8)
root.right.left = TreeNode(67)
root.right.right = TreeNode(161)
root.left.left.left = TreeNode(17)
root.left.left.right = TreeNode(43)
root.left.right.left = TreeNode(88)
root.left.right.right = TreeNode(37)

print(tree_to_array(root))
# [2, 7, 52, 13, 8, 67, 161, 17, 43, 88, 37]