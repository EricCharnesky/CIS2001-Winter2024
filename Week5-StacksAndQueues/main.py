# First In - First Out
# Last in - last out

import queue

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


stack_of_fries = Stack()

stack_of_fries.push("some fries")
stack_of_fries.push("more fries")
stack_of_fries.push("more fries")
stack_of_fries.push("more fries")
stack_of_fries.push("more fries")
stack_of_fries.push("more fries")
while not stack_of_fries.is_empty():
    print(stack_of_fries.pop())