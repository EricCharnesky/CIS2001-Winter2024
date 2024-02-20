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
            total += child.number_of_items()

        return total

    def depth(self):
        depth = 0
        current = self
        while current.parent is not None:
            current = current.parent
            depth += 1

    def height(self):
        if len(self.children) == 0:
            return 0
        return 1 + max(child.height() for child in self.children)

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