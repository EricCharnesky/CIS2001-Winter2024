class LinkedList:

    class Node:

        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self._first = None
        self._last = None
        self._number_of_items = 0

    def __len__(self):
        return self._number_of_items

    # O ( 1 )
    def append(self, data):
        if self._first is None:
            self._first = self.Node(data)
            self._last = self._first
        else:
            self._last.next = self.Node(data)
            self._last = self._last.next

        self._number_of_items += 1

    # O( k ) - really O(n)
    def insert(self, data, index):
        if self._first is None:
            raise IndexError
        if index > self._number_of_items:
            raise IndexError
        if index == self._number_of_items:
            self.append(data)
        elif index == 0:
            new_node = self.Node(data, self._first )
            self._first = new_node
            self._number_of_items += 1
        else:
            current_node = self._first
            for node in range(index-1): # stops 1 before the desired index
                current_node = current_node.next
            new_node = self.Node(data, current_node.next)
            current_node.next = new_node
            self._number_of_items += 1

    def front(self):
        return self._first.data

    # O( k[index] ) - really O(n)
    def get_item_at_index(self, index):
        self._check_for_valid_index(index)
        current_node = self._first

        # walking the nodes from the first to the index
        for node in range(index):
            current_node = current_node.next

        return current_node.data

    # O ( k ) which is really O (n)
    def pop(self, index):
        self._check_for_valid_index(index)
        if index == 0:
            data = self._first.data
            if self._first == self._last:
                self._last = None
            self._first = self._first.next
        else:
            current_node = self._first
            for node in range(index - 1):  # stops 1 before the desired index
                current_node = current_node.next
            data = current_node.next.data
            current_node.next.data = None # make sure the node doesn't store the data
            current_node.next = current_node.next.next
            if index == self._number_of_items - 1:
                self._last = current_node

        self._number_of_items -= 1
        return data

    def _check_for_valid_index(self, index):
        if index >= self._number_of_items:
            raise IndexError


class DoublyLinkedList:

    class Node:

        def __init__(self, data, next=None, previous=None):
            self.data = data
            self.next = next
            self.previous = previous

    def __init__(self):
        self._first = None
        self._last = None
        self._number_of_items = 0

    def __len__(self):
        return self._number_of_items

    # O ( 1 )
    def append(self, data):
        if self._first is None:
            self._first = self.Node(data)
            self._last = self._first
        else:
            self._last.next = self.Node(data, previous=self._last)
            self._last = self._last.next

        self._number_of_items += 1

    # O( k ) - really O(n)
    def insert(self, data, index):
        if self._first is None:
            raise IndexError
        if index > self._number_of_items:
            raise IndexError
        if index == self._number_of_items:
            self.append(data)
        elif index == 0:
            new_node = self.Node(data, next=self._first )
            self._first = new_node
            self._number_of_items += 1
        else:
            current_node = self._first
            for node in range(index-1): # stops 1 before the desired index
                current_node = current_node.next
            new_node = self.Node(data, next=current_node.next, previous=current_node)
            new_node.previous.next = new_node
            new_node.next.previous = new_node

            self._number_of_items += 1

    def front(self):
        return self._first.data

    # O( k[index] ) - really O(n)
    def get_item_at_index(self, index):
        # TODO - if index is closer to the end, walk backwards
        self._check_for_valid_index(index)
        current_node = self._first

        # walking the nodes from the first to the index
        for node in range(index):
            current_node = current_node.next

        return current_node.data

    # O ( k ) which is really O (n)
    def pop(self, index):
        self._check_for_valid_index(index)
        if index == 0:
            data = self._first.data
            if self._first == self._last:
                self._last = None
            self._first = self._first.next
        else:
            current_node = self._first
            for node in range(index - 1):  # stops 1 before the desired index
                current_node = current_node.next
            data = current_node.next.data
            current_node.next.data = None # make sure the node doesn't store the data
            current_node.next = current_node.next.next

            if index == self._number_of_items - 1:
                self._last = current_node
            else:
                # make sure that there is a valid current_node.next
                current_node.next.previous = current_node

        self._number_of_items -= 1
        return data

    def _check_for_valid_index(self, index):
        if index >= self._number_of_items:
            raise IndexError


class CircularDoublyLinkedList:

    class Node:

        def __init__(self, data, next=None, previous=None):
            self.data = data
            self.next = next
            self.previous = previous

    def __init__(self):
        self._dummy_node = self.Node(None)
        # dummy_node next is always the first item
        self._dummy_node.next = self._dummy_node

        # dummy_node previous is always the last item
        self._dummy_node.previous = self._dummy_node
        self._number_of_items = 0

    def __len__(self):
        return self._number_of_items

    # O ( 1 )
    def append(self, data):
        # last item's next will be the dummy node
        self._dummy_node.previous = (
            self.Node(data,
                      next=self._dummy_node,
                      previous=self._dummy_node.previous))

        self._number_of_items += 1

    # O( k ) - really O(n)
    def insert(self, data, index):
        if index > self._number_of_items:
            raise IndexError
        if index == self._number_of_items:
            self.append(data)
        else:
            current_node = self._dummy_node
            for node in range(index-1): # stops 1 before the desired index
                current_node = current_node.next
            new_node = self.Node(data, next=current_node.next, previous=current_node)
            new_node.previous.next = new_node
            new_node.next.previous = new_node

            self._number_of_items += 1

    def front(self):
        return self._dummy_node.data

    # O( k[index] ) - really O(n)
    def get_item_at_index(self, index):
        # TODO - if index is closer to the end, walk backwards
        self._check_for_valid_index(index)
        current_node = self._first

        # walking the nodes from the first to the index
        for node in range(index):
            current_node = current_node.next

        return current_node.data

    # O ( k ) which is really O (n)
    def pop(self, index):
        self._check_for_valid_index(index)

        current_node = self._dummy_node
        for node in range(index):  # stops 1 before the desired index
            current_node = current_node.next
        data = current_node.data
        current_node.data = None # make sure the node doesn't store the data
        current_node.next.previous = current_node.previous
        current_node.previous.next = current_node.next
        self._number_of_items -= 1
        return data

    def _check_for_valid_index(self, index):
        if index >= self._number_of_items:
            raise IndexError



class PositionalCircularDoublyLinkedList:


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
    class Node:

        def __init__(self, data, next=None, previous=None):
            self.data = data
            self.next = next
            self.previous = previous

    def __init__(self):
        self._dummy_node = self.Node(None)
        # dummy_node next is always the first item
        self._dummy_node.next = self._dummy_node

        # dummy_node previous is always the last item
        self._dummy_node.previous = self._dummy_node
        self._number_of_items = 0

    def _validate(self, position):
        if not isinstance(position, self.Position):
            raise TypeError
        if self is not position._container:
            raise ValueError
        if position._node.next is None:
            raise ValueError
        return position._node


    def _make_position(self, node):
        if node == self._dummy_node:
            return None
        return self.Position(self, node)

    def _add_between(self, data, next_node, previous_node):
        new_node = self.Node(data, next=next_node, previous=previous_node )
        new_node.previous.next = new_node
        new_node.next.previous = new_node
        self._number_of_items += 1
        return new_node

    # O(1)
    def first(self):
        return self._make_position(self._dummy_node.next)

    # O(1)
    def last(self):
        return self._make_position(self._dummy_node.previous)

    # O(1)
    def before(self, position):
        node = self._validate(position)
        return self._make_position(node.previous)

    # O(1)
    def after(self, position):
        node = self._validate(position)
        return self._make_position(node.next)

    # O(1)
    def add_after(self, position, data):
        node = self._validate(position)
        return self._make_position(self._add_between(data, previous_node=node, next_node=node.next))

    # O(1)
    def add_before(self, position, data):
        node = self._validate(position)
        return self._make_position(self._add_between(data, next_node=node, previous_node=node.previous))


    def __iter__(self):
        current = self.first()

        while current is not None:
            yield current.data()
            current = self.after(current)

    # O(1)
    def __len__(self):
        return self._number_of_items

    # O(1)
    def add_last(self, data):
        # last item's next will be the dummy node
        return self._make_position( \
            self._add_between(data, next_node=self._dummy_node, previous_node=self._dummy_node.previous))

    # O(1)
    def add_first(self, data):
        return self._make_position( \
            self._add_between(data, next_node=self._dummy_node.next, previous_node=self._dummy_node))

    # O(1)
    def delete(self, position):
        node = self._validate(position)
        # next_node = node.next
        # next_node.previous = node.previous
        node.next.previous = node.previous
        node.previous.next = node.next
        node.next = None # marks as invalid
        self._number_of_items -= 1
        return node.data


students = PositionalCircularDoublyLinkedList()
eric_position = students.add_first("Eric")
jeb_position = students.add_last("Jeb")
david_position = students.add_last("David")

john_position = students.add_before(david_position, "John")

for student in students:
    print(student)

numbers = PositionalCircularDoublyLinkedList()
for n in range(10_000_000):
    numbers.add_last(n)