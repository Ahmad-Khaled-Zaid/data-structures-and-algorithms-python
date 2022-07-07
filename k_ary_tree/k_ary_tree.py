class TNode:
    def __init__(self, value):
        self.value = value
        self.left = []
        self.right = []


class KArrTree:
    def __init__(self):
        self.root = None
        self.max = 0