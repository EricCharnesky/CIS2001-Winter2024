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
