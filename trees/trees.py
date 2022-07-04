class TNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.max = 0

    def pre_order(self):
        arr = []

        def _walk(root):
            print(root.value)
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

    def max_tree(self):
        self.max = self.root.value

        def _walk(root):
            if root.value > self.max:
                self.max = root.value
            if root.left:
                _walk(root.left)
            if root.right:
                _walk(root.right)

        _walk(self.root)
        return self.max


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
    search_tree = BinaryTree()
    search_tree.root = TNode(-1)
    search_tree.root.right = TNode(-5)
    search_tree.root.left = TNode(43)
    search_tree.root.left.right = TNode(-42)
    # search_tree.root.left.left = TNode()
    search_tree.pre_order()
    print(search_tree.max_tree())
