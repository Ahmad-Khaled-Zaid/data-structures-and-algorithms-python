class TNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        arr = []

        def _walk(root):
            # print(root.value)
            arr.append(root.value)
            if root.left:
                _walk(root.left)
            if root.right:
                _walk(root.right)

        _walk(self.root)
        return arr

    def in_order(self):
        arr = []

        def _walk(root):
            if root.left:
                _walk(root.left)
            arr.append(root.value)

            if root.right:
                _walk(root.right)

        _walk(self.root)
        return arr

    def post_order(self):
        arr = []

        def _walk(root):
            if root.left:
                _walk(root.left)

            if root.right:
                _walk(root.right)
            arr.append(root.value)

        _walk(self.root)
        return arr


class BinarySearchTree(BinaryTree):

    def add(self, value):
        node = TNode(value)
        root = self.root
        while root:
            if value >= root.value:
                if root.right is None:
                    root.right = node
                    break
                root = root.right

            elif value < root.value:
                if not root.left:
                    root.left = node
                    break
                root = root.left

    def contains(self, value):
        root = self.root
        while root:
            if root.value == value:
                return True
            if value >= root.value:
                if root.right is None:
                    return False
                root = root.right

            elif value < root.value:
                if not root.left:
                    return False
                root = root.left


if __name__ == "__main__":
    # tree = BinaryTree(TNode("A"))
    # tree.root.left = TNode("B")
    # tree.root.right = TNode("C")
    # tree.root.left = TNode("B")
    # tree.root.left.left = TNode("D")
    # tree.root.left.right = TNode("E")
    # tree.root.right.left = TNode("F")
    # tree.pre_order()
    # print("=" * 30)
    # tree.in_order()
    # print("=" * 30)
    # tree.post_order()
    search_tree = BinarySearchTree()
    search_tree.root = TNode(23)
    search_tree.add(42)
    search_tree.add(8)
    search_tree.add(4)
    search_tree.add(16)
    search_tree.add(15)
    search_tree.add(22)
    search_tree.add(27)
    search_tree.add(85)
    search_tree.add(105)
    print(search_tree.pre_order())
    print("=" * 30)
    # search_tree.in_order()
    # print(search_tree.contains(105))/
