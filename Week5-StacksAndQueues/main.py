# First In - First Out
# Last in - last out

import queue

class CircularDeque:

    INITIAL_SIZE = 10

    def __init__(self):
        self._data = [None] * self.INITIAL_SIZE
        self._front = 0
        self._back = 0
        self._number_of_items = 0

    def _resize(self, new_size):
        new_data = [None] * new_size
        if self._back > self._front:
            items_in_data = self._back - self._front
        else:
            items_in_data = len(self._data) - self._front + self._back
        new_data_index = 0
        if self._front < self._back:
            for index in range(self._front, self._back):
                new_data[new_data_index] = self._data[index]
                new_data_index += 1
        else:
            for index in range(self._front, len(self._data)):
                new_data[new_data_index] = self._data[index]
                new_data_index += 1
            for index in range(0, self._back):
                new_data[new_data_index] = self._data[index]
                new_data_index += 1
        self._data = new_data
        self._front = 0
        self._back = items_in_data



    # average O(1)
    # worst O(n)
    def add_back(self, item):
        self._check_capacity()
        self._data[self._back] = item
        self._back += 1
        if self._back == len(self._data):
            self._back = 0
        self._number_of_items += 1

    def _check_capacity(self):
        if self._number_of_items == len(self._data):
            self._resize(len(self._data) * 2)

    def add_front(self, item):
        self._check_capacity()
        self._front -= 1
        if self._front < 0:
            self._front = len(self._data) - 1
        self._data[self._front] = item

        self._number_of_items += 1



    # average O(1)
    # TODO - resize smaller
    def remove_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        item = self._data[self._front]
        self._data[self._front] = None
        self._front += 1
        if self._front == len(self._data):
            self._front = 0
        self._number_of_items -= 1
        return item

    def remove_back(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        self._back -= 1
        if self._back < 0:
            self._back = len(self._data) - 1
        item = self._data[self._back]
        self._data[self._back] = None
        self._number_of_items -= 1
        return item

    # average O(1)
    def front(self):
        if self.is_empty():
            raise IndexError
        return self._data[self._front]

    def back(self):
        if self.is_empty():
            raise IndexError
        return self._data[self._back - 1]

    def is_empty(self):
        return self._front == self._back

    def __len__(self):
        return self._number_of_items




# better memory usage than FasterQueue
class CircularQ:

    INITIAL_SIZE = 10

    def __init__(self):
        self._data = [None] * self.INITIAL_SIZE
        self._front = 0
        self._back = 0

    def _resize(self, new_size):
        new_data = [None] * new_size
        if self._back > self._front:
            items_in_data = self._back - self._front
        else:
            items_in_data = len(self._data) - self._front + self._back
        new_data_index = 0
        if self._front < self._back:
            for index in range(self._front, self._back):
                new_data[new_data_index] = self._data[index]
                new_data_index += 1
        else:
            for index in range(self._front, len(self._data)):
                new_data[new_data_index] = self._data[index]
                new_data_index += 1
            for index in range(0, self._back):
                new_data[new_data_index] = self._data[index]
                new_data_index += 1
        self._data = new_data
        self._front = 0
        self._back = items_in_data

    # average O(1)
    # worst O(n)
    def enqueue(self, item):
        self._data[self._back] = item
        self._back += 1
        if self._back == len(self._data):
            self._back = 0
        if self._back == self._front:
            self._resize(len(self._data) * 2)


    # average O(1)
    # TODO - resize smaller
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        item = self._data[self._front]
        self._data[self._front] = None
        self._front += 1
        if self._front == len(self._data):
            self._front = 0
        return item

    # average O(1)
    def front(self):
        return self._data[self._front]

    def is_empty(self):
        return self._front == self._back

class FasterQueue:

    def __init__(self):
        self._data = []
        self._front = 0

    # average O(1)
    # worst O(n)
    def enqueue(self, item):
        self._data.append(item)

    # average O(1)
    # traded increased space usage
    def dequeue(self):
        item = self._data[self._front]
        self._data[self._front] = None
        self._front += 1
        return item


    # average O(1)
    def front(self):
        return self._data[self._front]

    def is_empty(self):
        return len(self._data) == 0

class Queue:

    def __init__(self):
        self._data = []

    # average O(1)
    # worst O(n)
    def enqueue(self, item):
        self._data.append(item)

    # average O(n)
    def dequeue(self):
        return self._data.pop(0)

    # average O(1)
    def front(self):
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0


# Last In - First Out
# First In - Last Out
class Stack:

    def __init__(self):
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    # average O(1) - constant
    # worst O(n)
    def push(self, item):
        self._data.append(item)

    # average O(1)
    # worst O(1)
    def peek(self):
        return self._data[-1]

    # average O(1)
    # worst O(n)
    def pop(self):
        return self._data.pop()




deck = CircularDeque()

deck.add_front(1)
deck.add_back(10)
deck.add_front(0)

print(f'front: {deck.front()}')
print(f'back: {deck.back()}')

print('taking from back')
while not deck.is_empty():
    print(deck.remove_back())

deck.add_back(7)
deck.add_back(14)
deck.add_front(49)

print('taking from front')
while not deck.is_empty():
    print(deck.remove_front())


stack_of_fries = Stack()

stack_of_fries.push("some fries")
stack_of_fries.push("more fries")
stack_of_fries.push("more fries")
stack_of_fries.push("more fries")
stack_of_fries.push("more fries")
stack_of_fries.push("more fries")
while not stack_of_fries.is_empty():
    print(stack_of_fries.pop())