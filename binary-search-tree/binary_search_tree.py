class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)


class BinarySearchTree:
    def __init__(self, tree_data):
        self.sort = []
        self.root = None
        for value in tree_data:
            self.insert(value)

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            node = self.root
            while node:
                if node.data >= value:
                    if not node.left:
                        node.left = TreeNode(value)
                        node = None
                    else:
                        node = node.left
                else:
                    if not node.right:
                        node.right = TreeNode(value)
                        node = None
                    else:
                        node = node.right

    def data(self):
        return self.root

    def sorted_data(self):
        self.in_order(self.root, self.sort)
        return self.sort

    def in_order(self, root, sort):
        if root:
            self.in_order(root.left, sort)
            sort.append(root.data)
            self.in_order(root.right, sort)
