
class BinarySearchTree:

    class BinaryTreeNode:

        def __init__(self, data, parent = None, left_child = None, right_child = None):
            self.data = data
            self.parent = parent
            self.left_child = left_child
            self.right_child = right_child

    def __init__(self, data):
        self._root = BinarySearchTree.BinaryTreeNode(data)
        self._number_of_items = 1

    def _insert(self, data, node):
        if node.data == data:
            raise ValueError("Can't have duplicates in this tree")
        if data < node.data:
            if node.left_child is None:
                node.left_child = self.BinaryTreeNode(data, node)
            else:
                self._insert(data, node.left_child)
        else:
            if node.right_child is None:
                node.right_child = self.BinaryTreeNode(data, node)
            else:
                self._insert(data, node.right_child)

    # assuming we have somewhat of a full structure, we get O(log(n))
    def insert(self, data):
        self._insert(data, self._root)

    def _contains(self, data, node):
        if data == node.data:
            return True
        if data < node.data:
            if node.left_child is None:
                return False
            return self._contains(data, node.left_child)
        if node.right_child in None:
            return False
        return self._contains(data, node.right_child)

    # assuming we have somewhat of a balanced structure, we get O(log(n))
    def contains(self, data):
        return self._contains(data)

    # assuming we have somewhat of a full structure, we get O(log(n))
    def remove(self, data):
        # find the data, then replace with the largest smaller item
        # left child then all the way right