class Tree:

    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.children = []

    def add_child(self, data):
        self.children.append(Tree(data, self))

    def number_of_items(self):
        total = 1
        for child in self.children:
            total += child._number_of_items()

        return total

    def depth(self):
        depth = 0
        current = self
        while current.parent is not None:
            current = current.parent
            depth += 1
        return depth

    def height(self):
        if len(self.children) == 0:
            return 0
        return 1 + max(child.height() for child in self.children)



class PositionalLinkedBinaryTree:


    class Position:

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def data(self): # book calls it element
            return self._node.data

        # from book
        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    class BinaryTreeNode:

        def __init__(self, data, parent = None, left_child = None, right_child = None):
            self.data = data
            self.parent = parent
            self.left_child = left_child
            self.right_child = right_child

    def __init__(self, data):
        self._root = PositionalLinkedBinaryTree.BinaryTreeNode(data)
        self._number_of_items = 1

    def _validate(self, position):
        if not isinstance(position, self.Position):
            raise TypeError
        if self is not position._container:
            raise ValueError
        if position._node.parent is position._node:
            raise ValueError
        return position._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def root(self):
        return self._make_position(self._root)

    def left(self, position):
        return self._make_position(self._validate(position).left_child)

    def right(self, position):
        return self._make_position(self._validate(position).right_child)

    def sibling(self, position):
        node = self._validate(position)
        parent = node.parent
        if parent is None:
            return None
        if node == parent.left_child:
            return self._make_position(parent.right_child)
        return self._make_position(parent.left_child)

    def parent(self, position):
        return self._make_position(self._validate(position).parent)

    def children(self, position):
        if self.left(position) is not None:
            yield self.left(position)
        if self.right(position) is not None:
            yield self.right(position)

    def add_left(self, position, data):
        node = self._validate(position)
        if node.left_child is not None:
            raise ValueError("Already has a left")
        node.left_child = PositionalLinkedBinaryTree(data, parent=self)
        self._number_of_items += 1
        return self._make_position(node.left_child)

    def add_right(self, position, data):
        node = self._validate(position)
        if node.right_child is not None:
            raise ValueError("Already has a right")
        node.right_child = PositionalLinkedBinaryTree(data, parent=self)
        self._number_of_items += 1
        return self._make_position(node.right_child)

    def replace(self, position, data):
        node = self._validate(position)
        old_data = node.data
        node.data = data
        return old_data

    def delete(self, position):
        node = self._validate(position)
        if node.left_child is not None and node.right_child is not None:
            raise ValueError("Can't delete with 2 children")
        left_child = node.left_child
        right_child = node.right_child
        old_data = node.data

        if left_child is not None:
            node.data = left_child.data
            left_child.parent = left_child
            node.left_child = None
        elif right_child is not None:
            old_data = node.data
            node.data = right_child.data
            right_child.parent = right_child
            node.right_child = None
        else:
            if node.parent.right_child == node:
                node.parent.right_child = None
            else:
                node.parent.left_child = None
                node.parent = node

        self._number_of_items -= 1
        return old_data

    def __len__(self):
        return self._number_of_items

    def number_of_children(self, position):
        node = self._validate(position)
        children = 0
        if node.left_child is not None:
            children += 1
        if node.right_child is not None:
            children += 1

        return children

    def depth(self, position):
        node = self._validate(position)
        depth = 0
        current = node
        while current.parent is not None:
            current = current.parent
            depth += 1
        return depth

    def _height(self, position):
        if self.number_of_children(position) == 0:
            return 0
        return 1 + max(self._height(child) for child in self.children(position))

    def height(self, position = None):
        if position is None:
            position = self.root()
        return self._height(position)




binaryTree = PositionalLinkedBinaryTree(10)

root = binaryTree.root()

left = binaryTree.add_left( root, 5)
right = binaryTree.add_right(root, 15)

binaryTree.add_right(right, 25 )



tree = Tree(1)
tree.add_child(2)
tree.add_child(3)
two = tree.children[0]
two.add_child(4)
four = two.children[0]
four.add_child(5)
five = four.children[0]
five.add_child(8)
tree.add_child(6)
three = tree.children[1]
three.add_child(7)



print(f'number of items in tree: {tree.number_of_items()}')
print(f'height of tree: {tree.height()}')

print(f'height of tree 4: {four.height()}')