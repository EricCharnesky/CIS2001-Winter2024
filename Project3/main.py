# https://github.com/EricCharnesky/CIS2001-Winter2024/blob/main/Week5-StacksAndQueues/main.py
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

    def __len__(self):
        return len(self._data)


# https://github.com/EricCharnesky/CIS2001-Winter2024/blob/main/Week5-StacksAndQueues/main.py
class CircularQueue:

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


class TransportMethod:

    def __init__(self, number, number_of_items_needed, one_way_time):
        self.number = number
        self.number_of_items_needed = number_of_items_needed
        self.time_until_fully_loaded = 0
        self.one_way_time = one_way_time
        self.number_of_items = 0

    def load_item(self, current_time):
        self.number_of_items += 1
        if self.number_of_items == self.number_of_items_needed:
            self.time_until_fully_loaded = current_time + self.one_way_time
        return current_time + self.one_way_time * 2


class Dock:

    def __init__(self, number_of_items_per_train, number_of_items_per_plane, train_items, plane_items):
        self.trains = [None]
        for index, value in enumerate(number_of_items_per_train):
            self.trains.append(TransportMethod(index+1, value, index+1))

        self.planes = [None]
        for index, value in enumerate(number_of_items_per_plane):
            self.planes.append(TransportMethod(index+1, value, (index+1)*5))

        self.train_items_queue_of_stacks = CircularQueue()
        current_stack = Stack()
        for index, train_item in enumerate(train_items):
            if len(current_stack) == 5:
                self.train_items_queue_of_stacks.enqueue(current_stack)
                current_stack = Stack()

            current_stack.push(train_item)

        self.train_items_queue_of_stacks.enqueue(current_stack)

        self.planes_items_queue = CircularQueue()
        for plane_item in plane_items:
            self.planes_items_queue.enqueue(plane_item)

    def load_trains(self):
        current_time = 0
        while not self.train_items_queue_of_stacks.is_empty():
            current_stack = self.train_items_queue_of_stacks.dequeue()
            while len(current_stack) != 0:
                train_item = current_stack.pop()
                current_time = self.trains[train_item].load_item(current_time)

    def load_planes(self):
        current_time = 0
        while not self.planes_items_queue.is_empty():
            plane_item = self.planes_items_queue.dequeue()
            current_time = self.planes[plane_item].load_item(current_time)


    def load_items(self):
        self.load_trains()
        self.load_planes()
        for train in self.trains[1:]:
            print(train.time_until_fully_loaded, end=' ')
        print()
        for plane in self.planes[1:]:
            print(plane.time_until_fully_loaded, end=' ')

dock = Dock([2, 7, 1], [3, 2], [2, 2, 2, 3, 1, 2, 2, 2, 1, 2], [2, 1, 1, 1, 2])
dock.load_items()
