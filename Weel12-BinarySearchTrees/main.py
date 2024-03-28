
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
        if node is None:
            return False
        if data == node.data:
            return True
        if data < node.data:
            return self._contains(data, node.left_child)
        return self._contains(data, node.right_child)

    # assuming we have somewhat of a balanced structure, we get O(log(n))
    def contains(self, data):
        return self._contains(data)


    def _swap_node(self, node, node_to_swap):
        parent = node.parent
        if parent.left_child == node:
            parent.left_child = node_to_swap
        else:
            parent.right_child = node_to_swap
        if node_to_swap is not None:
            node_to_swap.parent = parent

    def _remove(self, data, node):
        if node is None:
            raise ValueError("Not Found")
        if data == node.data:
            next_largest_smaller_node = node.left_child
            if next_largest_smaller_node is None:
                self._swap_node(node, node.right_child)
            else:
                while next_largest_smaller_node.right_child is not None:
                    next_largest_smaller_node = next_largest_smaller_node.right_child
                value = next_largest_smaller_node.data
                self._swap_node(next_largest_smaller_node, next_largest_smaller_node.left_child)
                node.data = value

        if data < node.data:
            return self._remove(data, node.left_child)
        else:
            return self._remove(data, node.right_child)


    # assuming we have somewhat of a full structure, we get O(log(n))
    def remove(self, data):
        # find the data, then replace with the largest smaller item
        # left child then all the way right
        self._remove(data, self._root)

    def _print_in_order(self, node):
        if node.left_child:
            self._print_in_order(node.left_child)
        print(node.data)
        if node.right_child:
            self._print_in_order(node.right_child)
    def print_in_order(self):
        self._print_in_order(self._root)


values = BinarySearchTree(7)
values.insert(2)
values.insert(6)
values.insert(5)
values.insert(0)
values.insert(1)
values.insert(11)
values.insert(9)

values.print_in_order()